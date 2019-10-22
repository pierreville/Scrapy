CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "racquetlab.csv" DEL "racquetlab.csv"
scrapy crawl racquetlab -o racquetlab.csv
START racquetlab.csv