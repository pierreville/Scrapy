CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "controlthet.csv" DEL "controlthet.csv"
scrapy crawl controlthet -o controlthet.csv
START controlthet.csv
