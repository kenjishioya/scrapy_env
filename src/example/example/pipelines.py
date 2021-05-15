# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sys
sys.path.append('../')
from dao.connectMysql import MySQLConnector
import os

class ExamplePipeline:
    def open_spider(self, spider):
        self.connector = MySQLConnector()
        self.connector.execute_sqlfile('create_quotes.sql')

    def close_spider(self, spider):
        self.connector.close()

    def process_item(self, item, spider):
        parameters = (
            item.get('quote'),
            item.get('author'),
            item.get('tags')
        )
        self.connector.execute_sqlfile('insert_quotes.sql', parameters)
        return item
