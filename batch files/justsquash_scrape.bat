CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "justsquash.csv" DEL "justsquash.csv"
scrapy crawl justsquash -o justsquash.csv
START justsquash.csv