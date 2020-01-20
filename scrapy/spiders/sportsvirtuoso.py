import scrapy
from scrapyproduct.items import ScrapyproductItem


class SportsVirtuosoSpider(scrapy.Spider):
    name = "sportsvirtuoso"
    store_url = "https://sportsvirtuoso.com/en/"
    start_urls = [
    	#all
    	#'https://sportsvirtuoso.com/en/squash',
    	#rackets by brand
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/black-knight-squash',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/xamsa',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/dunlop',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/tecnifibre',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/harrow',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/oliver',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/prince',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/karakal',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/salming',
        'https://sportsvirtuoso.com/en/squash/racquets/by-brand/head-en',
        #balls
        'https://sportsvirtuoso.com/en/squash/balls',
        #grips
        'https://sportsvirtuoso.com/en/squash/grips-and-overgrips',
        #bags
        'https://sportsvirtuoso.com/en/squash/bags',
        #strings
        'https://sportsvirtuoso.com/en/squash/strings',
        #court shoes men
        'https://sportsvirtuoso.com/en/squash/mens-court-shoes',
        #court shoes women
        'https://sportsvirtuoso.com/en/squash/womens-court-shoes-en',
        #juniors
        'https://sportsvirtuoso.com/en/squash/juniors',
    ]

    seen_url = set()

    def parse(self, response):

        for item in response.css('div.products li.product div.product a.product-item-link'):

            url = item.css('a::attr(href)').extract_first()

            if url in self.seen_url:
            	continue
            self.seen_url.add(url)

            aff_title_raw = item.css('a::text').extract_first()

            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': aff_title_raw.strip(),
                #'title': response.css('h1.page-title span::text').extract_first(),
            }

        #find other pages to crawl
        #for item in response.css('div.main div.apptrian-subcategories-category-image'):
            #more_url = response.urljoin(item.css('a::attr(href)').extract_first())
            #yield scrapy.Request(more_url, callback=self.parse)