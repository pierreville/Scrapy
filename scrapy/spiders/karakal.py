import scrapy

class KarakalSpider(scrapy.Spider):
    name = "karakal"
    start_urls = [
        'https://www.karakal.com/squash/squash-rackets?limit=all',
    ]

    def parse(self, response):
        for item in response.css('div.category-products ul.products-grid li.item h2.product-name'):
            yield {
                'aff_url': response.urljoin(item.css('a::attr(href)').extract_first()),
                'aff_title': item.css('a::text').extract_first(),
            }


#        next_page = response.css('ul.pagination li a[title*="layout.pagination.next_html"]::attr(href)').extract_first()
#        
#        if next_page is not None:
#            next_page = response.urljoin(next_page)
#            yield scrapy.Request(next_page, callback=self.parse)