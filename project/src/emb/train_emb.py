import argparse
import os

from gensim.models import word2vec
import jieba
from nltk.tokenize import word_tokenize
from opencc import OpenCC
cc = OpenCC('s2twp') # Taiwan phrase; this aligns with the dict from MUSE


def parse_args():
    parser = argparse.ArgumentParser(description='Train word embeddings for multiple corpora.')
    parser.add_argument('--corpora', type=str, nargs='+', required=True,
                        help='The list of corpora files to train.')
    parser.add_argument('--dim', type=int, default=300,
                        help='The word embedding dimension. Default: 300')
    parser.add_argument('--epochs', type=int, default=5,
                        help='Number of epochs to train. Default: 5')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    for corpus in args.corpora:
        lang = corpus.split('_')[2]
        sents = word2vec.LineSentence(corpus)

        print('Training model...')
        model = word2vec.Word2Vec(sents, min_count=2, size=args.dim, iter=args.epochs)

        print('Saving model...')
        filename = '_'.join(os.path.splitext(corpus)[0].split('_')[:-1])
        model.save(filename + '.bin')
        model.wv.save_word2vec_format(filename + '.vec')

        print('Done {}'.format(corpus))
