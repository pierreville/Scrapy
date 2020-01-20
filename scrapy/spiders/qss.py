import scrapy

class QssSpider(scrapy.Spider):
    name = "qss"
    start_urls = [
        'https://www.qss-squash.nl/squash-rackets',
        'https://www.qss-squash.nl/squash-schoenen',
        'https://www.qss-squash.nl/grips-ballen',
        'https://www.qss-squash.nl/squash-tassen',
        #'https://www.qss-squash.nl/kleding',
        'https://www.qss-squash.nl/squash-snaren',
        'https://www.qss-squash.nl/squash-brillen',
        'https://www.qss-squash.nl/accessoires/squashracket-bumpers',

    ]

    def parse(self, response):
        for item in response.css('div.column.main div.product-item-details'):

            full = item.css('a.product-item-link::text').extract_first()

            yield {
                'aff_url': item.css('a.product-item-link::attr(href)').extract_first(),
                'aff_title': full.strip(),
                'aff_id': item.css('div.price-box::attr(data-product-id)').extract_first(),
            }

        next_page = response.css('li.pages-item-next a::attr(href)').extract_first()
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)
