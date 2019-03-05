import re


def num_human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format(round(num), ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def is_chinese(text):
    return len(re.findall('[\u4e00-\u9fff]+', text)) > 0

def has_letters(text):
    return len(re.findall('[a-zA-Z]+', text)) > 0

def always_true(x):
    return True
