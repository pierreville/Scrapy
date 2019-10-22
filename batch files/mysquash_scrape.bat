cd "F:\Dropbox\Bitbucket\scrapy\crawlers\scrapyproduct\"
IF EXIST "mysquash.csv" del "mysquash.csv"
scrapy crawl mysquash -o mysquash.csv
START mysquash.csv