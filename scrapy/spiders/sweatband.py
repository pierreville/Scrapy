# -*- coding: utf-8 -*-
import scrapy
import os

from scrapy.spiders import CSVFeedSpider
from urlparse import urlparse

from scrapyproduct.items import ScrapyproductItem


class SweatBandSpider(CSVFeedSpider):
    name = "sweatband"
    seen_product_url = set()
    white_list_category = ['court shoes', 'squash balls',
                           'squash eyewear', 'squash rackets']

    headers = [ 'aw_deep_link', 'product_name', 'aw_product_id', 'merchant_product_id',
                'merchant_image_url', 'description', 'merchant_category', 'search_price',
                'merchant_name', 'merchant_id', 'category_name', 'category_id',
                'aw_image_url', 'currency', 'store_price', 'delivery_cost',
                'merchant_deep_link', 'language', 'last_updated',
                'display_price', 'data_feed_id']

    def start_requests(self):
        #dir_path = os.path.dirname(os.path.realpath(__file__))
        #dir_path = "%s/csv/datafeed_150002.csv" % dir_path
        dir_path = "Scrapy/crawlers/scrapyproduct/scrapyproduct/spiders/csv/datafeed_150002.csv"
        return [scrapy.Request("file:///%s" % dir_path)]

    def parse_row(self, response, row):
        if row['merchant_category'].lower() in self.white_list_category:
            item = ScrapyproductItem()
            qs = urlparse(row['merchant_deep_link'])
            item['aff_url'] = qs.scheme + "://" + qs.netloc + qs.path
            if item['aff_url'] in self.seen_product_url:
                return
            self.seen_product_url.add(item['aff_url'])
            item['aff_title'] = row['product_name']
            item['aff_id'] = row['aw_product_id']
            yield item