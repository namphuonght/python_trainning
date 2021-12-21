import scrapy
import json


url = []
with open('list_url.json') as f:
    for line in json.load(f):
        url.append(line['url'])


class CrawlTextSpider(scrapy.Spider):
    name = 'crawl_text'
    start_urls = url

    def parse(self, response):
        yield {
            "text" : response.body
        }
        
    