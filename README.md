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
$ python -m project.src.data.scrape --arxiv [LANG ...] --gs [LANG ...]
# e.g.
$ python -m project.src.data.scrape --arxiv zh en --gs zh
# outputs
# project/data/<site>_<user-lang>_<lang>_<max-sent>.txt
```

Train embeddings:

```bash
$ python -m project.src.emb.train_emb --corpora [CORPUS_PATH ...]
# e.g.
$ python -m project.src.emb.train_emb --corpora project/data/arxiv_en_en_100.txt project/data/google-scholar_zh_zh_100.txt
# outputs
# project/data/<corpus-file-name>.bin, project/data/<corpus-file-name>.vec
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

### Sites

- [arXiv.org](https://arxiv.org/)
  - Support scraping papers of source or target languages.
  - Support scraping papers of non-native language users using institutes and last names as filters.
- [Google Scholar](https://scholar.google.com/scholar)
  - Support scraping papers of source or target languages only.

## Credits

Thanks to Facebook AI Research for their open-sourced code of [MUSE](https://github.com/facebookresearch/MUSE).