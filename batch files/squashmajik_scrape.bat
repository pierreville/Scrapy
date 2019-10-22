CD "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct"
IF EXIST "squashmajik.csv" DEL "squashmajik.csv"
scrapy crawl squashmajik -o squashmajik.csv
START squashmajik.csv