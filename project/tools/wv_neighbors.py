import sys

from gensim.models import KeyedVectors


if __name__ == '__main__':
    wv_file = sys.argv[1]
    wv = KeyedVectors.load_word2vec_format(wv_file)
    while True:
        word = input('Enter a word (enter qq to end): ')
        if word == 'qq':
            break
        else:
            print(wv.similar_by_word(word))
