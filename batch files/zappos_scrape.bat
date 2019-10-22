CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "zappos.csv" DEL "zappos.csv"
scrapy crawl zappos -o zappos.csv
START zappos.csv
