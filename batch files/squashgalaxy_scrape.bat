CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "squashgalaxy.csv" DEL "squashgalaxy.csv"
scrapy crawl squashgalaxy -o squashgalaxy.csv
START squashgalaxy.csv