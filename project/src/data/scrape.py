import argparse
import sys
import os

from paperscraper.scraper import Scraper
import marisa_trie

from ..utils.const import LAST_NAMES, INSTITUTE_NAMES, CATS


FILTER_BYS = ['institute', 'name', 'both']  # deciding factors of a native language background
L2_LANGS = ['en', 'zh']                     # native language options of users
TARGET_LANGS = ['en']                       # target language options
N_AUTHORS = 2                               # number of authors to consider
SAVE_PATH_DIR = 'project/data'              # data directory
LOG_PATH_DIR = 'project/output/logs'        # log directory

def parse_args():
    parser = argparse.ArgumentParser(description='Scrape all data.')
    parser.add_argument('--langs', type=str, nargs='+', required=True,
                        help='The native languages of users to scrape. Use language code2 to specify, e.g. en for English, zh for Chinese.')
    parser.add_argument('--target-lang', type=str, default='en',
                        help='The target language. Use language code2 to specify, e.g. en for English, zh for Chinese. Default: en')
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

    # Create classification filters
    if args.filter_by not in FILTER_BYS:
        print('filter by must be either one in {}'.format(FILTER_BYS))
        sys.exit()

    classifications = []
    for lang in args.langs:
        if lang not in L2_LANGS:
            print('language must be in {}'.format(L2_LANGS))
            sys.exit()
        
        classifications.append(create_filter(lang, args.filter_by))
 
    meta_filters = create_meta_filter(args.langs)

    # Determine sites to scrape from by target language
    if args.target_lang == 'en':
        site = 'arxiv'
    else:
        print('target language must be in {}'.format(TARGET_LANGS))
        sys.exit()

    # Create save paths
    save_paths = [os.path.join(SAVE_PATH_DIR, '{}_{}.txt'.format(lang, args.target_lang)) for lang in args.langs]
    log_path = os.path.join(LOG_PATH_DIR, '{}.log'.format(site))

    # Scrape for each category until max sentence count reached
    sent_cnts = [0] * len(classifications)
    termination_reached = [False] * len(classifications)
    for category in CATS:
        scraper = Scraper(
            category=category, date_from='2001-01-01', date_until='2018-12-31', max_sent=args.max_sent,
            classifications=classifications, filters=meta_filters
        )
        this_sent_cnts = scraper.scrape_text(site, save_to=save_paths, log_to=log_path, day_intv=5, append=True)

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

    print('Done.')
