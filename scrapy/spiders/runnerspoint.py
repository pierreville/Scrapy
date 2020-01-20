import scrapy
from scrapyproduct.items import ScrapyproductItem


class RunnersPointSpider(scrapy.Spider):
    name = "runnerspoint"
    store_url = "https://www.runnerspoint.com"
    start_urls = [
        'https://www.runnerspoint.com/en/men/shoes/sportshoes/indoorshoes/',
        'https://www.runnerspoint.com/en/women/shoes/sportshoes/indoorshoes/',
    ]
    seen_product_url = set()

    def parse(self, response):
        for row in response.css('div.fl-category--productlist--item'):
            url = row.css('a::attr(href)').extract_first()
            if url in self.seen_product_url:
                continue
            self.seen_product_url.add(url)
            item = ScrapyproductItem()
            item['aff_url'] = url
            item['aff_title'] = row.css('a>span::text').extract_first()
            item['aff_id'] = row.css('div.fl-load-animation::attr(data-scroll-to-target)').re('\-(\d+)')[0]
            yield item