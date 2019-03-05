import argparse
import os

from gensim.models import Word2Vec
import jieba
from nltk.tokenize import word_tokenize
from opencc import OpenCC
cc = OpenCC('s2twp') # Taiwan phrase; this aligns with the dict from MUSE


def parse_args():
    parser = argparse.ArgumentParser(description='Train word embeddings for multiple corpora.')
    parser.add_argument('--corpora', type=str, nargs='+', required=True,
                        help='The list of corpora files to train.')
    parser.add_argument('--dim', type=int, default=300,
                        help='The word embedding dimension.')

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

if __name__ == '__main__':
    args = parse_args()

    for corpus in args.corpora:
        lang = corpus.split('_')[2]
        sents = load_corpus(corpus, lang)

        print('Building model...')
        model = Word2Vec(min_count=2, size=args.dim)
        model.build_vocab(sents)

        print('Training model...')
        model.train(sents, total_examples=model.corpus_count, epochs=model.iter)

        print('Saving model...')
        filename = os.path.splitext(corpus)[0]
        model.save(filename + '.bin')
        model.wv.save_word2vec_format(filename + '.vec')

        print('Done {}'.format(corpus))
