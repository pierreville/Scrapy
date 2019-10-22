CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "dlsports.csv" DEL "dlsports.csv"
scrapy crawl dlsports -o dlsports.csv
START dlsports.csv