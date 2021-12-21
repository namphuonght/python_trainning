# -*- coding: utf-8 -*-
import scrapy


class UrlPostSpider(scrapy.Spider):
    name = 'url_post'
    start_urls = ['https://blog.ycombinator.com/']

    def parse(self, response):
        for post in response.css("div[class='loop-section']"):          
            yield {
                "url" : post.css("a[class='article-title']::attr('href')").extract_first()
            }
            
        next_page = response.css("#content-section > div.inner-content-section.grid-pct-65 >\
                                div.archive-nav.grid-col-16.clearfix >\
                                div.nav-previous > a::attr('href')").extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )   