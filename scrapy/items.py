# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyproductItem(scrapy.Item):
    # define the fields for your item here like:
    aff_url = scrapy.Field()
    aff_title = scrapy.Field()
    aff_id = scrapy.Field()
