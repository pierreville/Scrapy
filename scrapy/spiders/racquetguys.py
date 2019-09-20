import scrapy
from scrapyproduct.items import ScrapyproductItem


class RacquetGuysSpider(scrapy.Spider):
    name = "racquetguys"
    store_url = "https://racquetguys.com"
    start_urls = [
        #rackets
        'https://racquetguys.com/collections/black-knight-squash-racquets',
        'https://racquetguys.com/collections/dunlop-squash-racquets',
        'https://racquetguys.com/collections/harrow-squash-racquets',
        'https://racquetguys.com/collections/head-squash-racquets',
        'https://racquetguys.com/collections/karakal-squash-racquets',
        'https://racquetguys.com/collections/prince-squash-racquets',
        'https://racquetguys.com/collections/prokennex-squash-racquets',
        'https://racquetguys.com/collections/salming-squash-racquets',
        'https://racquetguys.com/collections/tecnifibre-squash-racquets',
        'https://racquetguys.com/collections/wilson-squash-racquets',
        #'https://racquetguys.com/collections/doubles-squash-racquets',
        #men's shoes
        'https://racquetguys.com/collections/asics-mens-squash-shoes',
        'https://racquetguys.com/collections/babolat-mens-squash-shoes',
        'https://racquetguys.com/collections/head-mens-squash-shoes',
        'https://racquetguys.com/collections/salming-womens-squash-shoes',
        'https://racquetguys.com/collections/yonex-mens-squash-shoes',
        #women shoes
        'https://racquetguys.com/collections/asics-womens-squash-sheos',
        'https://racquetguys.com/collections/head-womens-squash-shoes',
        'https://racquetguys.com/collections/salming-womens-squash-shoes',
        'https://racquetguys.com/collections/yonex-womens-squash-shoes',
        #strings
        'https://racquetguys.com/collections/ashaway-squash-strings',
        'https://racquetguys.com/collections/dunlop-squash-strings',
        'https://racquetguys.com/collections/gamma-squash-strings',
        'https://racquetguys.com/collections/harrow-squash-strings',
        'https://racquetguys.com/collections/head-squash-strings',
        'https://racquetguys.com/collections/prince-squash-strings',
        'https://racquetguys.com/collections/salming-squash-strings',
        'https://racquetguys.com/collections/tecnifibre-squash-strings',
        #balls
        'https://racquetguys.com/collections/squash-balls-1',
        #bags
        'https://racquetguys.com/collections/salming-squash-bags',
        'https://racquetguys.com/collections/tecnifibre-squash-bags',
        'https://racquetguys.com/collections/black-knight-squash-bags',
        'https://racquetguys.com/collections/dunlop-squash-bags',
        'https://racquetguys.com/collections/harrow-squash-bags',

        ]

    def parse(self, response):
        for item in response.css('div.product-image'):

            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('img::attr(alt)').extract_first(),
            }
