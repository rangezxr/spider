# -*- coding: utf-8 -*-

import pymongo
from pymongo.collection import Collection

class Connect_mongo(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='192.168.1.100',port=27017)
        self.db_data = self.client['dou_guo_mei_shi']

    def insert_item(self,item):
        db_collection = self.db_data['dou_guo_mei_shi_item']
        db_collection.insert(item)


mongo_info = Connect_mongo()
