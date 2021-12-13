"""
Build web crawler function
"""


# =============================================================================


__auth__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/13'
__status__ = 'development'


# =============================================================================


import argparse
from bs4 import BeautifulSoup
import requests
import logging
import string
import re


logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s')


# =============================================================================


def get_args():
    """Parse CLI arguments from users

    Returns:
        (object) : Arguments parsed from CLI
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', '-u', type=str,
            help='The URL want to crawl')
    return parser.parse_args()


# =============================================================================


def crawler(url):
    html = requests.get(url)
    raw = BeautifulSoup(html.content, 'html.parser')
    title = raw.find_all('h1', {'class':'title-detail'})
    paper = raw.find_all('p', {'class':'Normal'})
    return title, paper


# =============================================================================


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', str(text))


# =============================================================================


def save_file(args):
    title_raw, paper_raw = crawler(args.url)
    title, paper = remove_tags(title_raw), remove_tags(paper_raw)
    
    f = open('my_data.txt', 'w', encoding='utf-8')
    f.write(title + paper)
    f.close


# =============================================================================


if __name__ == '__main__':
    logging.info('Task: Crawling data\n')

    args = get_args()
    save_file(args)
    logging.info('Process Done')

