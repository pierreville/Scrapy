import scrapy
from scrapyproduct.items import ScrapyproductItem
import json
from scrapy.selector import Selector

class ZalandoSpider(scrapy.Spider):
    name = "zalando"
    store_url = "https://www.zalando.co.uk"
    start_urls = [
        'https://www.zalando.co.uk/mens-sports-shoes/?sport_type=handball.volleyball.badminton&order=activation_date',
        'https://www.zalando.co.uk/womens-sports-shoes/?sport_type=handball.volleyball.badminton&order=activation_date',
        'https://www.zalando.co.uk/kids-indoor-sports-shoes/?sport_type=handball.volleyball',
    ]
    seen_product_url = set()

    def parse(self, response):
        # for row in response.css('z-grid.z-nvg-cognac_articles>z-grid-item'):
        #     url = response.urljoin(row.css('a.z-nvg-cognac_imageLink-OPGGa::attr(href)').extract_first())
        #     if url in self.seen_product_url:
        #         continue
        #     self.seen_product_url.add(url)
        #     item = ScrapyproductItem()
        #     item['aff_url'] = url
        #     item['aff_title'] = "%s %s" % (
        #         row.css('div.z-nvg-cognac_brandName-2XZRz::text').extract_first(),
        #         row.css('div.z-nvg-cognac_articleName--arFp::text').extract_first())
        #     item['aff_id'] = row.css('span.sku::text').extract_first()
        #     yield item
        # next_page = response.css('a.z-nvg-cognac_link-8qswi::attr(href)').extract()[1]
        # if next_page:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page)

        ##### Edited by Nouman Awais ######
        sel=Selector(response)
        json_data="".join(sel.xpath('//script[@id="z-nvg-cognac-props"]/text()').extract()).strip()
        try:
            json_data=json_data.split('![CDATA')[1].strip().split('}}]]')[0]+"}}]"
            json_data=json.loads(json_data)
            for j in json_data:
                articles=j['articles']
                for a in articles:
                    url=a['url_key']
                    if url in self.seen_product_url:
                        continue
                    self.seen_product_url.add(url)
                    item = ScrapyproductItem()
                    item['aff_url'] ="https://www.zalando.co.uk/" + url+".html"
                    item['aff_title'] = "%s %s" % (
                        a['brand_name'],
                        a['name'])
                    item['aff_id'] = a['sku']
                    yield item
                    
                try:
                    next_page = j['next_page_path']
                    if next_page:
                        next_page = response.urljoin(next_page)
                        yield scrapy.Request(next_page)
                except:
                    pass
            
        except:
            pass