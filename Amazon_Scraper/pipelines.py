# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3
# class AmazonScraperPipeline:
#     def __init__(self):
#         self.con=sqlite3.connect("data.db")
#         self.cur=self.con.cursor()
#         self.create_table()

#     def create_table(self):
#         self.cur.execute("""DROP TABLE IF EXISTS amazon_data""")
#         self.cur.execute("""CREATE TABLE amazon_data( 
#             Product_Name text ,
#             Product_URL text,
#             Product_Price REAL,
#             Product_Description text
#             )""")

#     def process_item(self, item, spider):
#         print("pipeline",item["Product_name"])
#         print(item["Product_url"])
#         self.cur.execute("""INSERT INTO amazon_data values(?,?,?,?)"""
#         (item["Product_name"],
#         item["Product_url"],
#         item["Product_price"],
#         item["Product_description"])
#         )
#         self.con.commit()
        return item
