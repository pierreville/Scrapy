import scrapy

class MySquashSpider(scrapy.Spider):
    name = "mysquash"
    start_urls = [
        'https://www.my-squash.com/fr/raquette-squash/',
        'https://www.my-squash.com/fr/chaussure-squash/',
    ]

    def parse(self, response):
        for item in response.css('a.product_img_link'):
            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': item.css('a::attr(title)').extract_first(),
            }