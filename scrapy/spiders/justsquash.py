import scrapy

class justsquashSpider(scrapy.Spider):
    name = "justsquash"
    start_urls = [
        'https://www.just-squash.co.uk/shop/rackets/squash-rackets.html',
        'https://www.just-squash.co.uk/shop/shoes/mens-squash-shoes.html',
        'https://www.just-squash.co.uk/shop/shoes/women-s-shoes.html',

    ]

    def parse(self, response):
        for item in response.css('section#prodthumbnails a'):
            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': item.css('div.name h2::text').extract_first(),
            }

        next_page = response.xpath('//span[@class="next"]/../@href').extract_first()
        if next_page is not None:
           yield scrapy.Request(next_page, callback=self.parse)