from django.shortcuts import render
from pymongo import MongoClient
from django.core.paginator import Paginator

# Create your views here.
client = MongoClient('localhost',27017)
db=client.test
#arti_info为表名
collection=db.arti_info

paginator=Paginator(db.arti_info.limit)
for item in collection.find()[:1]:
    context={
        'title':item['title'],
    }


def index(request):
    return render(request,'index.html',context)