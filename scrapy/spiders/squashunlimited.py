import scrapy

class SquashUnlimitedSpider(scrapy.Spider):
    name = "squashunlimited"

    start_urls = [
        'https://www.squashunlimited.ca/product-category/squash/squash-racquets/',
        'https://www.squashunlimited.ca/product-category/squash/squash-shoes/',
        'https://www.squashunlimited.ca/product-category/squash/squash-bags',
        'https://www.squashunlimited.ca/product-category/squash-grips',
        'https://www.squashunlimited.ca/product-category/squash-string-service',
        'https://www.squashunlimited.ca/product-category/squash-training-injury/',
        'https://www.squashunlimited.ca/product-category/squash-eyewear',
        'https://www.squashunlimited.ca/product-category/squash-balls',
    ]

    def parse(self, response):

        for snuh in response.css('h3.product-name'):
            yield {
                'aff_title': snuh.css('a::text').extract_first(),
                'aff_url': snuh.css('a::attr(href)').extract_first(),
            }

        next_page = response.css('a.next::attr(href)').extract_first()

        if next_page is not None:
            yield scrapy.Request(next_page,callback=self.parse)