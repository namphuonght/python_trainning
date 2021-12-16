import os
import argparse
import logging
import requests
from bs4 import BeautifulSoup
import re

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s')


# =============================================================================


__auth__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/16'
__status__ = 'development'


# =============================================================================


def get_args():
    """Parse CLI arguments from users

    Returns:
        (object) : Arguments parsed from CLI
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', '-p', type=str,
            help='The path want to crawl')
    return parser.parse_args()


# =============================================================================


def load_list_url(data_path):
    urls = []
    
    with open(data_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            urls.append(line)


    return urls


# =============================================================================


def crawler(url):
    html = requests.get(url)
    raw = BeautifulSoup(html.content, 'html.parser')
    content = raw.find_all('p', {'class':'Normal'})
    return content


# =============================================================================


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', str(text))


# =============================================================================


def save_file(args):
    urls = load_list_url(args.path)
    contents = []
    for url in urls:
        contents.append(remove_tags(crawler(url)))
    f = open('content_list.txt', 'w', encoding='utf-8')
    f.write(str(contents))
    f.close


# =============================================================================


if __name__ == '__main__':

    logging.info('Task: Crawling data\n')
    args = get_args()
    save_file(args)
    logging.info('Process Done')


# =============================================================================
