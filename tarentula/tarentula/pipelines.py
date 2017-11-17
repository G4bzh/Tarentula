# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class TarentulaPipeline(object):
    # def process_item(self, item, spider):
        # return item

import json

class FilePipeline(object):

    def __init__(self, outfile):
        self.outfile=outfile

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            outfile=crawler.settings.get('OUTPUT_FILE'),
        )
        
    def open_spider(self, spider):
        self.file = open(self.outfile, 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item

