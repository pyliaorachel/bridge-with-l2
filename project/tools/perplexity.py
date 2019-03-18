import argparse
import os
import sys

from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import MLE


def parse_args():
    parser = argparse.ArgumentParser(description='Calculate perplexity of given corpora.')
    parser.add_argument('--train', type=str, required=True,
                        help='The training corpora.')
    parser.add_argument('--corpora', type=str, nargs='+', required=True,
                        help='The list of corpora files to compute perplexity.')
    parser.add_argument('--n', type=int, default=2,
                        help='The n of the n-gram model. Default: 2')

    args = parser.parse_args()
    return args

def load_corpus(corpus_file):
    text = []
    with open(corpus_file, 'r') as fin:
        for line in fin:
            text.append(word_tokenize(line))
    return text

if __name__ == '__main__':
    args = parse_args()

    lm = MLE(2)

    train_corpus = load_corpus(args.train)
    train, vocab = padded_everygram_pipeline(2, train_corpus)
    lm.fit(train, vocab)

    for test in args.corpora:
        test_corpus = load_corpus(test)
        print('{}: {}'.format(test, lm.perplexity(test_corpus)))
