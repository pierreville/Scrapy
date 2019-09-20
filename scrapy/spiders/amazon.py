import scrapy

class AmazonSpider(scrapy.Spider):
    name = "amazon"
    start_urls = [
        'https://scraper.pierrebastien.net/us/volleyball-shoes-men/',
        'https://scraper.pierrebastien.net/us/squash-shoes-men/',
        'https://scraper.pierrebastien.net/us/volleyball-shoes-women/',
        'https://scraper.pierrebastien.net/us/black-knight-squash-rackets/', 
        'https://scraper.pierrebastien.net/us/dunlop-squash-rackets/',
        'https://scraper.pierrebastien.net/us/harrow-squash-rackets/',
        'https://scraper.pierrebastien.net/us/head-squash-rackets/',
        'https://scraper.pierrebastien.net/us/karakal-squash-rackets/',
        'https://scraper.pierrebastien.net/us/mantis-squash-rackets/',
        'https://scraper.pierrebastien.net/us/oliver-squash-rackets/',
        'https://scraper.pierrebastien.net/us/prince-squash-rackets/',
        'https://scraper.pierrebastien.net/us/prokennex/',
        'https://scraper.pierrebastien.net/us/salming-rackets-us/',
        'https://scraper.pierrebastien.net/us/tecnifibre-rackets-us/',
        'https://scraper.pierrebastien.net/us/unsquashable-rackets-us/',
        'https://scraper.pierrebastien.net/us/victor-rackets-us/',
        'https://scraper.pierrebastien.net/us/wilson-rackets-us/',
        'https://scraper.pierrebastien.net/us/xamsa-rackets-us/',
        'https://scraper.pierrebastien.net/us/squash-bags-us/',
        

    ]

    def parse(self, response):
        for item in response.css('span.product'):
            aff_title_raw = item.css('span.title::text').extract_first()

            yield {
                'aff_url': item.css('span.url::text').extract_first(),
                'aff_title': aff_title_raw.replace('"',''),
                'aff_id': item.css('span.asin::text').extract_first(),
            }