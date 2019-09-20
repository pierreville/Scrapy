import scrapy

#first download the webpage as HTML to F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct\scrapyproduct\spiders\html

class SquashmajikSpider(scrapy.Spider):
    name = "squashmajik"
    start_urls = [
        'file:///Dropbox/Bitbucket/scrapy/crawlers/scrapyproduct/scrapyproduct/spiders/html/squashmajik.html',
    ]

    def parse(self, response):
        for item in response.css('h3.lvtitle a.vip'):
            url=item.css('a::attr(href)').extract_first()
            question_mark=url.find('?')
            ebay_id=url[(question_mark - 12):(question_mark)]
            yield {
                'aff_url': url,
                'aff_id': ebay_id,
                'aff_title': item.css('a::text').extract_first(),
            }