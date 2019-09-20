# -*- coding: utf-8 -*-
import scrapy
from scrapyproduct.items import ScrapyproductItem

class PDHsportsspider(scrapy.Spider):
    name = "pdh"
    start_urls = (
        'https://www.pdhsports.com/c/q/squash/squash-rackets',
        'https://www.pdhsports.com/c/q/squash/squash-shoes',
        'https://www.pdhsports.com/c/q/squash/squash-bags',
        'https://www.pdhsports.com/c/q/squash/squash-balls',
        'https://www.pdhsports.com/c/q/squash/squash-grips',
        'https://www.pdhsports.com/c/q/squash/squash-strings',
        'https://www.pdhsports.com/c/q/squash/squash-goggles-and-protective-eyewear',
        'https://www.pdhsports.com/c/q/squash/junior-squash-rackets',
        'https://www.pdhsports.com/c/q/squash/junior-squash-shoes',
    )
    seen_product_url = set()

    def parse(self, response):
        product_url = set()
        for row in response.css('div.product'):
            url = row.xpath('./a/@href').extract()[0]
            url = response.urljoin(url)
            if url in self.seen_product_url:
                continue
            self.seen_product_url.add(url)

            product_url.add(url)
            title = row.css('div.product span.prod-name>a::text').extract_first()
            id = url.split("/")[5]
            item = ScrapyproductItem()
            item['aff_url'] = url
            item['aff_title'] = title
            item['aff_id'] = id
            yield item