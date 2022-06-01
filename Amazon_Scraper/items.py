# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScraperItem(scrapy.Item):
    Product_name = scrapy.Field()
    Product_url = scrapy.Field()
    Product_price = scrapy.Field()
    Product_description = scrapy.Field()
    pass
