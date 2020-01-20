# -*- coding: utf-8 -*-
import scrapy
import re
from scrapyproduct.items import ScrapyproductItem


class SpartooSpider(scrapy.Spider):
    name = "spartoo"
    store_url = "http://www.spartoo.co.uk"
    start_urls = (
        'http://www.spartoo.co.uk/Indoor-sports-trainers-men-sty-10218-10027-0.php',
        'http://www.spartoo.co.uk/Indoor-sports-trainers-women-sty-10217-10027-0.php',
    )
    seen_product_url = set()

    def parse(self, response):
        for row in response.css('div.display_product3'):
            url = row.xpath('./a/@href').extract()[0]
            url = "%s/%s" % (self.store_url, url)
            if url in self.seen_product_url:
                continue
            self.seen_product_url.add(url)
            title = " ".join(row.xpath('./a/span//text()').extract())
            id = re.findall('-x(.*)\.php', url)[0]
            item = ScrapyproductItem()
            item['aff_url'] = url
            item['aff_title'] = title
            item['aff_id'] = id
            yield item
        next_page = response.xpath('//a[@rel="next"]/@href').extract()
        if next_page:
            next_page = "%s/%s" % (self.store_url, next_page[0])
            yield scrapy.Request(next_page)