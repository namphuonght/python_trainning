import scrapy
from demo_scrapy.items import DemoScrapyItem

class MacbookTgddSpider(scrapy.Spider):
    name = 'macbook_tgdd'
    allowed_domains = ['www.thegioididong.com']
    start_urls = ['https://www.thegioididong.com/laptop-apple-macbook/']

    def parse(self, response):
        # Request tới từng sản phẩm có trong danh sách các Macbook dựa vào href
        for item_url in response.css("li.item > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(item_url), callback=self.parse_macbook) # Nếu có sản phẩm thì sẽ gọi tới function parse_macbook
        
       # nếu có sản phẩm kế tiếp thì tiếp tục crawl
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
    
    def parse_macbook(self, response):
        item = DemoScrapyItem()
        
        item['product_name'] = response.css(
            'body > section.detail > h1 ::text').extract_first() # Tên macbook
        
        out_of_stock = response.css('strong.productstatus ::text').extract_first() # Tình trạng còn hàng hay không
        if out_of_stock: 
            item['price'] = response.css(
            'body > section.detail > div.box_main > div.box_right > div.box04.notselling > div.price-one > div > p ::text').extract_first()
        else: 
            item['price'] = response.css(
            'body > section.detail > div.box_main > div.box_right > div.box04.notselling > div.price-one > div > p ::text').extract_first()
            
        discount_online = response.css('body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.giamsoc-ol > p').extract_first() # Check nếu có giảm giá khi mua online hay không
        if discount_online:
            item['price_sale'] = response.css(
                'body > section.detail > div.box_main > div.box_right > div.box04.box_normal > div.giamsoc-ol > div > p ::text').extract_first()
        else:
            item['price_sale'] = response.css(
                'body > section:nth-child(5) > div.box04.box_normal > div.price-one > div > p ::text').extract_first()
                
        item['rate_average'] = response.css('#danhgia > div.rating-star.left > div > div > p ::text').extract_first()

        yield item