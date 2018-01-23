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


import sqlite3
from contextlib import closing
import hashlib

class SqlitePipeline(object):

    def __init__(self, dbpath):
        self.dbpath=dbpath

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            dbpath=crawler.settings.get('DB_PATH'),
        )

    def open_spider(self, spider):
        try:

            self.conn = sqlite3.connect(self.dbpath)
            cursor = self.conn.cursor()
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS content(
            id TEXT PRIMARY KEY UNIQUE,
            url TEXT,
            title TEXT,
            retitle TEXT,
            thumb TEXT,
            posted INTEGER
            )
            """)
            self.conn.commit()

            cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_posted
            ON content(posted)
            """)
            self.conn.commit()

        except sqlite3.Error,e:
            raise Exception( "Error in pipeline open_spider: %s" % e)

        finally:
            cursor.close()            

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
        INSERT INTO content(id, url, title, retitle, thumb, posted) VALUES(?, ?, ?, ?, ?, ?)""", (hashlib.sha1(item['url']).hexdigest(), item['url'], item['title'], item['retitle'], item['thumb'], 0))
        
        except sqlite3.IntegrityError:
            # Key already exists (id est URL already scrapped), do nothing
            pass
        
        finally:
            self.conn.commit()
            cursor.close()
            return item



class SqliteTitlesPipeline(object):

    def __init__(self, dbpath):
        self.dbpath=dbpath

    @classmethod
    def from_crawler(cls, crawler):
        ## pull in information from settings.py
        return cls(
            dbpath=crawler.settings.get('DB_PATH'),
        )

    def open_spider(self, spider):
        try:

            self.conn = sqlite3.connect(self.dbpath)
            cursor = self.conn.cursor()
            
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS content(
            id TEXT PRIMARY KEY UNIQUE,
            title TEXT
            )
            """)
            self.conn.commit()

        except sqlite3.Error,e:
            raise Exception( "Error in pipeline open_spider: %s" % e)

        finally:
            cursor.close()            

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
        INSERT INTO content(id, title) VALUES(?, ?)""", (hashlib.sha1(item['url']).hexdigest(), item['title']))
        
        except sqlite3.IntegrityError:
            # Key already exists (id est URL already scrapped), do nothing
            pass
        
        finally:
            self.conn.commit()
            cursor.close()
            return item