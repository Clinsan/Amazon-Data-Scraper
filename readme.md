
# Amazon Data Scraper

Implemented a data scraper to scrape data from amazon links.

###  Spider Location:Amazon_Scraper/spider/scraper.py
#### Tools Used:Python, Anaconda, VS code
#### Library Used: scrapy, time, pandas
#### Output Json file :scraped_data.json

## Approach

* fetched the data from the csv file.
* Iterated over the data and appended and the links with country and asin in a list.
* Iterated over each link in the list and scraped the data from the links and yield a dictionary.
* calculated the time taken for every 100 entries.
* Stored the data in a json file.

## Installation

1) #### Install Anaconda

```bash
  https://www.anaconda.com/
```
2) #### Open terminal from the anaconda Navigator
4) #### Install Scrapy
```bash
conda install -c conda-forge scrapy
```
5) #### Generate Scrapy project
```bash
scrapy startproject Amazon_Scraper
```
6) #### Generate Scrapy spider
```bash
cd Amazon_Scraper
scrapy genspider scraper www.amazon.de
```

7) #### Open Project In VS Code
8) #### Open terminal in  VS Code
9) #### Install scrapy-fake-useragents
```bash
pip install scrapy-fake-useragent
```
10) #### Go to settings.py and paste the below code
```bash
  DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}
```
11) #### Run the spider and stor the output in a json file
```bash
  scrapy crawl scraper -o scraped_data.json
```

    