CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "pdhsports.csv" DEL "pdhsports.csv"
scrapy crawl pdh -o pdhsports.csv
START pdhsports.csv
