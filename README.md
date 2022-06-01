# Amazon-Data-Scraper
Spider Location:Amazon_Scraper/spider/scraper.py
Tools Used:Python,Anaconda,VS Code
Library Used:scrapy,time,pandas

Output Json file :scraped_data.json

Approach:
fetched the data from the csv file
Iterated over the data and appended and the links with country and asin in a list.
Iterated over each link in the list and scraped the data from the links and yield a dictionary
calculated the time taken for every 100 entries.
Stored the data in a json file

Instructions:
Install Anaconda
Install Scrapy
Generate Scrapy project
Generate Scrapy Spider
Open Project
Run the spider and stor the output in a json file
