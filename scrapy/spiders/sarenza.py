# -*- coding: utf-8 -*-
import scrapy
import re
from scrapyproduct.items import ScrapyproductItem

class SarenzaSpider(scrapy.Spider):
    name = "sarenza"
    store_url = "http://www.sarenza.co.uk"
    start_urls = (
        'http://www.sarenza.co.uk/homeuniverse.aspx?req=fh_location%253d%252f%252fcatalog01%252fen_GB%252fsarenzauniverse%253e%257b11%257d%252fglobalvisibility%253d1%252fluxe%253e%257b0%253b1%257d%252fpays%253den%252fsport%253d11%2526fh_sort_by%253d-publicationdate_sorting%2526fh_start_index%253d0%2526fh_view_size%253d99&products=true&isSelectionEngine=1&genderId=0&implicitcriterion=%7b%22sarenzauniverse%22%3a%7b%22Name%22%3a%22sarenzauniverse%22%2c%22Values%22%3a%5b%2211%22%5d%2c%22IsMulti%22%3atrue%2c%22IsInvert%22%3afalse%7d%2c%22luxe%22%3a%7b%22Name%22%3a%22luxe%22%2c%22Values%22%3a%5b%220%22%2c%221%22%5d%2c%22IsMulti%22%3atrue%2c%22IsInvert%22%3afalse%7d%2c%22globalvisibility%22%3a%7b%22Name%22%3a%22globalvisibility%22%2c%22Values%22%3a%5b%221%22%5d%2c%22IsMulti%22%3afalse%2c%22IsInvert%22%3afalse%7d%2c%22pays%22%3a%7b%22Name%22%3a%22pays%22%2c%22Values%22%3a%5b%22en%22%5d%2c%22IsMulti%22%3afalse%2c%22IsInvert%22%3afalse%7d%7d',
    )
    seen_product_url = set()

    def parse(self, response):
        for row in response.css('ul.prdctlst>li.itm'):
            url = row.xpath('./a/@href').extract()[0]
            if url in self.seen_product_url:
                continue
            self.seen_product_url.add(url)

            title = row.css('div.md>img::attr(alt)').extract_first()
            id = re.findall('-p0(.*)', url)[0]
            item = ScrapyproductItem()
            item['aff_url'] = url
            item['aff_title'] = title
            item['aff_id'] = id
            yield item
        next_page = response.css('li.nxt::attr(data-url)').extract_first()
        if next_page:
            next_page = "%s/Homewoman.aspx%s" % (self.store_url, next_page)
            yield scrapy.Request(next_page)