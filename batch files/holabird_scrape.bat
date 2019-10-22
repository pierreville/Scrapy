CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "holabird.csv" DEL "holabird.csv"
scrapy crawl holabird -o holabird.csv
START holabird.csv