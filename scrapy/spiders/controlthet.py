import scrapy

class ControltheTSpider(scrapy.Spider):
    name = "controlthet"
    start_urls = [
        'https://www.controlthet.com/squash?sort=newest',
    ]

    def parse(self, response):
        for item in response.css('li.product .card-title'):
            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': item.css('a::text').extract_first(),
            }

        next_page = response.css('div.pagination li.pagination-item--next a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)