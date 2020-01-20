import scrapy

class AmazonUKSpider(scrapy.Spider):
    name = "amazonuk"
    start_urls = [
        'https://scraper.pierrebastien.net/uk/',
    ]

    def parse(self, response):
        for item in response.css('span.product'):
            aff_title_raw = item.css('span.title::text').extract_first()

            yield {
                'aff_url': item.css('span.url::text').extract_first(),
                'aff_title': aff_title_raw.replace('"',''),
                'aff_id': item.css('span.asin::text').extract_first(),
            }

        for item in response.css('div.entry-content ul li.follow'):
            url = response.urljoin(item.css('a::attr(href)').extract_first())
            yield scrapy.Request(url, callback=self.parse)