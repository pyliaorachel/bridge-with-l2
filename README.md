# bridge-with-l2

In exploration of the bridging effect of an L2 corpus between source and target languages.

## Usage

Install dependencies:

```bash
$ pip install -r requirements.txt
```

Collect data:

```bash
$ python -m project.src.data.scrape --arxiv zh en --gs zh
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