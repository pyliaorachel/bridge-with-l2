# bridge-with-l2

In exploration of the bridging effect of an L2 corpus between source and target languages.

## Usage

Install dependencies:

```bash
# Without GPU:
$ conda env create -f environment.yml
# With GPU:
$ conda env create -f gpu_environment.yml

$ conda activate l2
$ python
>>> import nltk
>>> nltk.download('punkt')
```

Collect data:

```bash
$ python -m project.src.data.scrape --arxiv [LANG ...] --gs [LANG ...] --arxiv-filter-by [FILTER_BY ...]
# e.g.
$ python -m project.src.data.scrape --arxiv zh en-loose en --gs zh --arxiv-filter-by both institute both
# outputs
# project/data/<site>_<user-lang>_<lang>_<max-sent>.txt
```

Clean corpus (outputs each sentence as a list of space-separated tokens):

```bash
$ python -m project.src.emb.clean_corpus --corpora [CORPUS_PATH ...]
# e.g.
$ python -m project.src.emb.clean_corpus --corpora project/data/arxiv_en_en_100.txt project/data/google-scholar_zh_zh_100.txt
# outputs
# project/data/<corpus-file-name>_clean.txt
```

Train embeddings (on cleaned corpora):

```bash
# word2vec or fastText
$ python -m project.src.emb.train_emb --corpora [CORPUS_PATH ...] --method METHOD --epochs EPOCHS --min-count MIN_COUNT --dim DIM
# e.g.
$ python -m project.src.emb.train_emb --corpora project/data/arxiv_en_en_100_clean.txt project/data/google-scholar_zh_zh_100_clean.txt --method word2vec --epochs 5
# outputs
# project/data/<corpus-file-name>.bin, project/data/<corpus-file-name>.vec

# GloVe
$ cd project/src/emb/GloVe
$ ./demo.sh CORPUS_PATH EPOCHS DIM MIN_COUNT
# e.g.
$ ./demo.sh ../../../data/essay_zh_en_1M_clean.txt 20 200 5
# outputs
# vectors.txt, vocab.txt, vectors.bin, cooccurence.shuf.bin, cooccurrence.bin
```

MUSE train:

```bash
$ cd MUSE/data/
$ ./get_evaluation.sh
$ cd ../..

# See https://github.com/facebookresearch/MUSE for more options
$ python MUSE/unsupervised.py --src_lang SRC_LANG --tgt_lang TGT_LANG --src_emb SRC_EMB --tgt_emb TGT_EMB
# e.g. for large test, with CUDA
$ python MUSE/unsupervised.py --src_lang zh --tgt_lang en --src_emb project/data/google-scholar_zh_zh_1M.vec --tgt_emb project/data/arxiv_en_en_1M.vec --normalize_embeddings center --exp_name test-large
# e.g. for small test, without CUDA
$ python MUSE/unsupervised.py --src_lang zh --tgt_lang en --src_emb project/data/google-scholar_zh_zh_100.vec --tgt_emb project/data/arxiv_en_en_100.vec --cuda 0 --n_epochs 2 --dis_most_frequent 100 --epoch_size 64 --normalize_embeddings center --exp_name test-small
```

MUSE evaluate:

```bash
# See https://github.com/facebookresearch/MUSE for more options
$ python MUSE/evaluate.py --src_lang SRC_LANG --tgt_lang TGT_LANG --src_emb SRC_EMB --tgt_emb TGT_EMB
# e.g. for large test, with CUDA
$ python MUSE/evaluate.py --src_lang zh --tgt_lang en --src_emb MUSE/dumped/test-large/3ozzevm3ik/vectors-zh.txt --tgt_emb MUSE/dumped/test-large/3ozzevm3ik/vectors-en.txt --max_vocab 200000 --exp_name test-large-eval
# e.g. for small test, without CUDA
$ python MUSE/evaluate.py --src_lang zh --tgt_lang en --src_emb MUSE/dumped/test-small/3ozzevm3ik/vectors-zh.txt --tgt_emb MUSE/dumped/test-small/3ozzevm3ik/vectors-en.txt --max_vocab 500 --cuda 0 --exp_name test-small-eval
```

## Data

Sample data in `project/data/<site>_<user-native-lang>_<target-lang>_<max-sent>.txt`.
Sample logs in `project/output/logs/<site>_<max-sent>.log` or `project/output/logs/<site>_<lang>_<max-sent>.log`.

The categories, institutes, last names, and queries are specified in `project/src/utils/const.py`.

## Tools

Visualize of `train.log`:

```bash
$ python project/tools/visualize.py TRAIN_LOG
# e.g.
$ python project/tools/visualize.py MUSE/dumped/fasttext_wiki-zh-zh_wiki-en-en_epoch-size-250000_epoch-10/rrmor5rqvo/train.log
# outputs
# dis_loss_acc.png, precision.png, prediction.png under the same folder
```

Calculate perplexity:

```bash
$ python project/tools/perplexity.py [--train TRAIN_CORPUS] --corpora [TEST_CORPUS ...]
# e.g. has a training corpus
$ python project/tools/perplexity.py --train project/data/wiki.en.txt --corpora project/data/arxiv_zh_en_880K.txt project/data/arxiv_en_en_480K.txt
# e.g. use default training corpus
$ python project/tools/perplexity.py --corpora project/data/arxiv_zh_en_880K.txt project/data/arxiv_en_en_480K.txt
```

### Sites

- [arXiv.org](https://arxiv.org/)
  - Support scraping papers of source or target languages.
  - Support scraping papers of non-native language users using institutes and last names as filters.
- [Google Scholar](https://scholar.google.com/scholar)
  - Support scraping papers of source or target languages only.

## Credits

Thanks to Facebook AI Research for their open-sourced code of [MUSE](https://github.com/facebookresearch/MUSE).
