from django.db import models
from mongoengine import *
from pymongo import MongoClient
from mongoengine import connect

connect('website',host='127.0.0.1',port=27017)
client = MongoClient('localhost',27017)
#连接所需数据库test为数据库名
db=client.test
#arti_info为表名
collection=db.arti_info

collection.insert({'title':'Tom','des':'this is a description','score':'5.0','tags':'tag'})

# for item in (collection.find())[:1]:
#     print(item['title'])
