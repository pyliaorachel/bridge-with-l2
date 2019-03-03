import argparse
import sys
import os

from paperscraper.scraper import Scraper
import marisa_trie

from ..utils.const import LAST_NAMES, INSTITUTE_NAMES, CATS, QUERIES
from ..utils.utils import num_human_format, is_chinese, always_true


FILTER_BYS = ['institute', 'name', 'both']  # deciding factors of a native language background
ARXIV_LANGS = ['en', 'zh']                  # supported language users of corpora to scrape from arXiv
GOOGLE_SCHOLAR_LANGS = ['zh']               # supported language users of corpora to scrape from Google Scholar
N_AUTHORS = 2                               # number of authors to consider
SAVE_PATH_DIR = 'project/data'              # data directory
LOG_PATH_DIR = 'project/output/logs'        # log directory

def parse_args():
    parser = argparse.ArgumentParser(description='Scrape all data.')
    parser.add_argument('--arxiv', type=str, nargs='+', required=True,
                        help='The language users of arXiv papers to scrape. Use language code2 to specify, e.g. en for English, zh for Chinese.')
    parser.add_argument('--gs', type=str, nargs='+', required=True,
                        help='The language users of Google Scholar papers to scrape. Use language code2 to specify, e.g. en for English, zh for Chinese.')
    parser.add_argument('--filter-by', type=str, default='both',
                        help='The key to filter the papers, either "institute", "name", or "both". Default: both')
    parser.add_argument('--max-sent', type=int, default=100,
                        help='Maximum number of sentences to scrape for each type of corpus.')

    args = parser.parse_args()
    return args

def institute_filter(tup, names):
    text_list, institutes, meta, is_main_file = tup
    m = len(institutes)
    if not is_main_file:
        return True
    if m == 0:
        return False

    satisfy = [institute in names for institute in institutes]
    return sum(satisfy) >= min(m, N_AUTHORS)

def name_filter(tup, names):
    text_list, institutes, meta, is_main_file = tup
    m = len(meta['authors'])
    if m == 0:
        return False

    satisfy = [name in names for name in meta['authors']]
    return sum(satisfy) >= min(m, N_AUTHORS)

def create_filter(lang, filter_by):
    if filter_by == 'institute':
        names = marisa_trie.Trie(INSTITUTE_NAMES[lang])
        return lambda tup: institute_filter(tup, names)
    elif filter_by == 'name':
        names = marisa_trie.Trie(LAST_NAMES[lang])
        return lambda tup: name_filter(tup, names)
    elif filter_by == 'both':
        last_names = marisa_trie.Trie(LAST_NAMES[lang])
        institute_names = marisa_trie.Trie(INSTITUTE_NAMES[lang])
        return lambda tup: name_filter(tup, last_names) and institute_filter(tup, institute_names)

def create_meta_filter(langs):
    names = []
    for lang in langs:
        names += LAST_NAMES[lang]
    return { 'authors': marisa_trie.Trie(names) }

if __name__ == '__main__':
    args = parse_args()
    max_sent_str = num_human_format(args.max_sent)

    # arXiv site
    print('========== arXiv ==========')
    site = 'arxiv'

    ## Create classification filters
    if args.filter_by not in FILTER_BYS:
        print('filter by must be either one in {}'.format(FILTER_BYS))
        sys.exit()

    classifications = []
    for lang in args.arxiv:
        if lang not in ARXIV_LANGS:
            print('language must be in {}'.format(ARXIV_LANGS))
            sys.exit()
        
        classifications.append(create_filter(lang, args.filter_by))

    meta_filters = create_meta_filter(args.arxiv)

    ## Create save paths
    save_paths = [os.path.join(SAVE_PATH_DIR, '{}_{}_en_{}.txt'.format(site, lang, max_sent_str)) for lang in args.arxiv]
    log_path = os.path.join(LOG_PATH_DIR, '{}_{}.log'.format(site, max_sent_str))

    ## Scrape for each category until max sentence count reached
    sent_cnts = [0] * len(classifications)
    termination_reached = [False] * len(classifications)
    for category in CATS:
        scraper = Scraper(
            category=category, date_from='2001-01-01', date_until='2018-12-31', max_sent=args.max_sent,
            classifications=classifications, filters=meta_filters
        )
        this_sent_cnts = scraper.scrape_text(site, save_to=save_paths, log_to=log_path, day_intv=5, append=True)
        print('Sentence counts for {}: {}'.format(category, this_sent_cnts))

        # Update sentence counts
        for i in range(len(classifications)):
            sent_cnts[i] += this_sent_cnts[i]

        # Check termination
        for i, sent_cnt in enumerate(sent_cnts):
            if not termination_reached[i] and sent_cnt >= args.max_sent:
                classifications[i] = lambda x: False
                termination_reached[i] = True
        if all(termination_reached):
            break

    print('Done arXiv.')

    # Google Scholar site
    print('========== Google Scholar ==========')
    site = 'google-scholar'

    for lang in args.gs:
        if lang not in GOOGLE_SCHOLAR_LANGS:
            print('language must be in {}'.format(GOOGLE_SCHOLAR_LANGS))
            continue
        
        filter_text = always_true
        if lang == 'zh':
            filter_text = is_chinese

        ## Create queries
        queries = QUERIES[lang]

        ## Create save paths
        save_path = os.path.join(SAVE_PATH_DIR, '{}_{}_{}_{}.txt'.format(site, lang, lang, max_sent_str))
        log_path = os.path.join(LOG_PATH_DIR, '{}_{}_{}.log'.format(site, lang, max_sent_str))

        ## Scrape for each query until max sentence count reached
        scraper = Scraper(filter_text=filter_text, max_sent=args.max_sent)
        sent_cnt = scraper.scrape_text(site, queries=queries, save_to=save_path, log_to=log_path, append=True)
        print('Sentence count for {}: {}'.format(lang, sent_cnt))

    print('Done Google Scholar.')