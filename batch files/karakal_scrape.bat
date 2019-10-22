CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "karakal.csv" DEL "karakal.csv"
scrapy crawl karakal -o karakal.csv
START karakal.csv