CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "sportsvirtuoso.csv" DEL "sportsvirtuoso.csv"
scrapy crawl sportsvirtuoso -o sportsvirtuoso.csv
START sportsvirtuoso.csv