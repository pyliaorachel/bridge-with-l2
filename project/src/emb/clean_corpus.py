import argparse
import os

import jieba
from nltk.tokenize import word_tokenize
from opencc import OpenCC
cc = OpenCC('s2twp') # Taiwan phrase; this aligns with the dict from MUSE


def parse_args():
    parser = argparse.ArgumentParser(description='Clean multiple corpora.')
    parser.add_argument('--corpora', type=str, nargs='+', required=True,
                        help='The list of corpora files to train.')

    args = parser.parse_args()
    return args

def load_corpus(corpus_file, lang):
    with open(corpus_file, 'r') as fin:
        for line in fin:
            if lang == 'zh':
                line = cc.convert(line)
                tokens = jieba.lcut(line)
                tokens = [token for token in tokens if token != '\n' and token != ' ']
            else:
                tokens = word_tokenize(line.lower())
            yield tokens

def save_corpus(sents, output_file):
    with open(output_file, 'w') as fout:
        for sent in sents:
            print(' '.join(sent), file=fout)

if __name__ == '__main__':
    args = parse_args()

    for corpus in args.corpora:
        lang = corpus.split('_')[2]

        print('Cleaning corpus')
        sents = load_corpus(corpus, lang)

        print('Saving corpus...')
        filename = os.path.splitext(corpus)[0]
        save_corpus(sents, filename + '_clean.txt')

        print('Done {}'.format(corpus))
