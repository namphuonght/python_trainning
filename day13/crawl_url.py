"""
Build web crawler function
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
import re
import datetime


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
    parser.add_argument('--start_page', '-s', type=int,
            help='Start page', required=False)
    parser.add_argument('--end_page', '-e', type=int,
            help='End page', required=False)
    parser.add_argument('--start_day', '-sd', type=str,
            help='Start day', required=False)
    parser.add_argument('--end_day', '-ed', type=str,
            help='End day', required=False)
    return parser.parse_args()


# =============================================================================


def cvt_datetime_to_timestamp(time):
    """
    Function to convert from datetime to timestamp
    """
    date = datetime.datetime.strptime(time, f"%d/%m/%Y")
    timestamp = datetime.datetime.timestamp(date)

    return timestamp


# =============================================================================


def crawler_url(url):
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


def crawler_content(url):
    html = requests.get(url)
    raw = BeautifulSoup(html.content, 'html.parser')
    text = raw.text
    img_src = []
    for img in raw.find_all('img'):
        src = str(img.get('src'))
        if img not in img_src and src.startswith('https://i1'):
            img_src.append(src)
    return text, img_src


# =============================================================================


TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', str(text))


# =============================================================================


def save_file(args):
    if args.start_page and args.end_page:
        for n in range(args.start_page, args.end_page+1):
            urls = crawler_url(args.url+f'-p{n}')  
            for url in urls:
                text, img_src = crawler_content(url)
                f = open('list_content.txt', 'a', encoding='utf-8')
                f.write(str(text))
                for src in img_src:
                    file = open('list_img.txt', 'a', encoding='utf-8')
                    file.write(str(src)+'\n')
    f.close
    file.close


# =============================================================================


if __name__ == '__main__':
    
    args = get_args()
    save_file(args)
    logging.info('Process Done')
