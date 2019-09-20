import scrapy

class ControltheTSpider(scrapy.Spider):
    name = "racquetlab"
    start_urls = [
        'https://www.racquetlab.com/collections/squash',
    ]

    def parse(self, response):
        for item in response.css('div.product-title'):
            title_whitespace = item.css('a::text').extract_first()
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': title_whitespace.strip(),
            }

        next_page = response.urljoin(response.css('div.load_more a::attr(href)').extract_first())
        
        if next_page is not None:
            yield scrapy.Request(next_page, callback=self.parse)