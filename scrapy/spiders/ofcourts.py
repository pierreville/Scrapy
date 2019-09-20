import scrapy

class OfCourtsSpider(scrapy.Spider):
    name = "ofcourts"
    start_urls = [
        'https://ofcourts.com/store/View-All-c22793434', #rackets
        #'https://ofcourts.com/store/View-All-c22850251', #shoes - women
        #'https://ofcourts.com/store/View-All-c22837201', #shoes - men
        #'https://ofcourts.com/store/Junior-Squash-Shoes-c21231462',
        #'https://ofcourts.com/store/Racket-Bags-c21231465',
        #'https://ofcourts.com/store/Backpacks-c21231466',
        #'https://ofcourts.com/store/Ashaway-Strings-c21312736',
        #'https://ofcourts.com/store/Dunlop-Strings-c21312739',
        #'https://ofcourts.com/store/Head-Strings-c21412520',
        #'https://ofcourts.com/store/Tecnifibre-Strings-c21312737',
        #'https://ofcourts.com/store/Xamsa-Strings-c21312738',
        #'https://ofcourts.com/store/Squash-Replacement-Grips-c21436926',
        #'https://ofcourts.com/store/Squash-Overgrips-c21436925',
        #'https://ofcourts.com/store/Eyeguards-Goggles-c21692055',
        ]

    def parse(self, response):
        for item in response.css('a.grid-product__title'):
            yield {
                'aff_url': item.css('a::attr(href)').extract_first(),
                'aff_title': item.css('a::text').extract_first().strip(),
            }
