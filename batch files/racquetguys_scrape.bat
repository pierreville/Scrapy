CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "racquetguys.csv" DEL "racquetguys.csv"
scrapy crawl racquetguys -o racquetguys.csv
START racquetguys.csv