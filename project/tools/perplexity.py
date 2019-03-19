import argparse
import os
import sys

from nltk.corpus import brown
from nltk.tokenize import word_tokenize
from nltk.lm.preprocessing import padded_everygram_pipeline
from nltk.lm import Laplace


def parse_args():
    parser = argparse.ArgumentParser(description='Calculate perplexity of given corpora.')
    parser.add_argument('--train', type=str,
                        help='The training corpora. If not specified, the brown corpus is used.')
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
            line = line.strip()
            if line != '':
                text.append(word_tokenize(line))
    return text

def corpus_perplexity(corpus, lm):
    """
    Ref: https://stats.stackexchange.com/questions/129352/how-to-find-the-perplexity-of-a-corpus
    """
    log_p_ss = []
    n_gram_cnt = 0
    for sent in corpus:
        ngrams = [ngram for ngram in sent]
        log_p_s = lm.entropy(ngrams) * (-len(ngrams)) # sum log(p(w))
        log_p_ss.append(log_p_s)
        n_gram_cnt += len(ngrams)
    mean = sum(log_p_ss) / n_gram_cnt
    entropy = -1 * mean
    perplexity = pow(2.0, entropy)
    return perplexity

if __name__ == '__main__':
    args = parse_args()

    lm = Laplace(args.n) # smoothing

    if args.train is not None:
        train_corpus = load_corpus(args.train)
    else:
        train_corpus = brown.sents()
    train, vocab = padded_everygram_pipeline(args.n, train_corpus)
    lm.fit(train, vocab)

    for test_file in args.corpora:
        test_corpus = load_corpus(test_file)
        test, vocab = padded_everygram_pipeline(args.n, test_corpus)
        perplexity = corpus_perplexity(test, lm)
        print('{}: {}'.format(test_file, perplexity))
