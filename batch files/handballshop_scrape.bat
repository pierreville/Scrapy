CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "handballshop.csv" DEL "handballshop.csv"
scrapy crawl handballshop -o handballshop.csv
START handballshop.csv