"""
Build web crawler URL function
"""


# =============================================================================


__auth__ = 'Tran Nam Phuong'
__email__ = 'trannamphuong2k@gmail.com'
__date__ = '2021/12/16'
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
    soup = BeautifulSoup(html.content, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        path = str(link.get('href'))
        if path not in urls and path.startswith('https://vnexpress.net/')\
            and not re.search('#', path):
            logging.info(f'Crawling: {path}')
            urls.append(path)
    return urls


# =============================================================================


def save_file(args):
    urls = crawler(args.url)  
    for url in urls:
        f = open('list_url.txt', 'a', encoding='utf-8')
        f.write(str(url)+'\n')
    f.close


# =============================================================================


if __name__ == '__main__':
    
    args = get_args()
    save_file(args)
    logging.info('Process Done')
