CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "ofcourts.csv" DEL "ofcourts.csv"
scrapy crawl ofcourts -o ofcourts.csv
START ofcourts.csv