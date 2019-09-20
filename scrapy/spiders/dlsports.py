import scrapy
from scrapyproduct.items import ScrapyproductItem


class DlSportsSpider(scrapy.Spider):
    name = "dlsports"
    store_url = "https://www.dlsports.de"
    start_urls = [
    	#rackets
        'https://www.dlsports.de/head/dunlop/index.html',
        'https://www.dlsports.de/squash2/head/head/index.html',
        'https://www.dlsports.de/head/karakal/index.html',
        'https://www.dlsports.de/head/oliver/index.html',
        'https://www.dlsports.de/squash2/head/prince/index.html',
        'https://www.dlsports.de/squash2/head/tecnifibre/index.html',
        'https://www.dlsports.de/squash2/head/wilson/index.html',
        'https://www.dlsports.de/squash2/head/zateq/index.html',
        #other
        'https://www.dlsports.de/squash2/grip-bands/index.html', #grips
        'https://www.dlsports.de/squash2/squash-zubehor/index.html', #goggles
        'https://www.dlsports.de/squash2/balls/dunlop/index.html', #balls
        #bags
        'https://www.dlsports.de/tennis2/tennisschlaeger/index.html',
        'https://www.dlsports.de/tennis2/tecnifibre/index.html',
        #shoes
        'https://www.dlsports.de/shoes/hi-tec/index.html',
        'https://www.dlsports.de/shoes/prince2/index.html',
        #strings
        'https://www.dlsports.de/strings/ashaway/index.html',
        'https://www.dlsports.de/strings/oliver/index.html',
        'https://www.dlsports.de/strings/tecnifibre/index.html',
        'https://www.dlsports.de/strings/zateq/index.html',
    ]
    seen_product_url = set()

    def parse(self, response):
        for row in response.css('.product-list .pl-row'):
            url = response.urljoin(row.css('h4 a::attr(href)').extract_first())
            if url in self.seen_product_url:
                continue
            self.seen_product_url.add(url)
            item = ScrapyproductItem()
            item['aff_url'] = url
            item['aff_title'] = row.css('h4 a::text').extract_first()
            item['aff_id'] = row.css('div.pl-cell::attr(data-pkid)').extract_first()
            yield item