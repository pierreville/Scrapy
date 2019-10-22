CD "F:\Dropbox\Bitbucket\Scrapy\crawlers\scrapyproduct"
IF EXIST "squashunlimited.csv" DEL "squashunlimited.csv"
scrapy crawl squashunlimited -o squashunlimited.csv
START squashunlimited.csv