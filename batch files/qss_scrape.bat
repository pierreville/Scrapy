CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "qss.csv" DEL "qss.csv"
scrapy crawl qss -o qss.csv
START qss.csv
