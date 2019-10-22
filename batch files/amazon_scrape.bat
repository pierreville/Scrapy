CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "amazon.csv" DEL "amazon.csv"
scrapy crawl amazon -o amazon.csv
START amazon.csv
