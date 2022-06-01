from itertools import count, product

from requests import Response
import scrapy
import pandas as pd
from ..items import AmazonScraperItem
import time
url_list=[]
count=1
df=pd.read_csv(r"C:\Users\clins\projects\Amazon_Scraper\Amazon_Scraper\Amazon Scraping - Sheet1.csv")
a=df.Asin.tolist()
c=df.country.tolist()
rrr=[]
t=[]
z=[]
p=[]
d=[]
p_l=[]
for i in range(1,len(a)):
    url_list.append("https://www.amazon.{country}/dp/{asin}".format(country=c[i],asin=a[i]))

class ScraperSpider(scrapy.Spider):
    name = 'scraper'
    start_urls = ['http://www.amazon.de/dp/000004458X']


    def parse(self, response):
            global count
            item=AmazonScraperItem()
            if response.status==404:
                resp=str(response)
                Product_title=Product_image_URL=Product_Price=Product_details="{url} IS NOT AVAILABLE".format(url=resp[4:len(resp)-1])


            else:
                begin=time.time()
                Product_title=response.css("#productTitle::text").get()

                Product_image_URL=response.xpath("//*[(@id = 'landingImage')]/@src").get()
                if Product_image_URL==None:
                    Product_image_URL=response.xpath('//*[(@id = "imgBlkFront")]/@src').get()

                Product_Price=response.css(".a-price-whole::text").get()
                if Product_Price==None:

                    Product_Price=response.css("#price::text").get()
                if Product_Price==None:

                    Product_Price=response.css("#usedBuySection .a-text-normal").css("::text").get()

                Product_details=response.css("#bookDescription_feature_div span").css("::text").get()
                if Product_details==None:
       

                    Product_details=response.css("#feature-bullets li").css("::text").get()
                if Product_details=="\n":

                    Product_details=response.css("#apEligibility_feature_div").css("::text").get()

                for url in url_list:
                    if count==100:
                        end=time.time()
                        print("TIME TAKEN TO COMPLETE IS ",end-begin)
                        count=0
                    else:
                        count=count+1

                        
                    yield scrapy.Request(url,callback=self.parse)
            item["Product_name"]=Product_title
            item["Product_url"]=Product_image_URL
            item["Product_price"]=Product_Price
            item["Product_description"]=Product_details

            yield item

