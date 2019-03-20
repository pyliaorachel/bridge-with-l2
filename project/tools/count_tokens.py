import argparse
import os


def parse_args():
    parser = argparse.ArgumentParser(description='Calculate number of tokens of given clean corpora.')
    parser.add_argument('--corpora', type=str, nargs='+', required=True,
                        help='The list of clean corpora files to count tokens.')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    for corpus in args.corpora:
        token_cnt = 0
        with open(corpus, 'r') as fin:
            for line in fin:
                token_cnt += len(line.split(' '))
        print('{}: {}'.format(corpus, token_cnt))
