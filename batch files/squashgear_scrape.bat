CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "squashgear.csv" DEL "squashgear.csv"
scrapy crawl squashgear -o squashgear.csv
START squashgear.csv