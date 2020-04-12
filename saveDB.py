import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def get_GangNam():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://store.naver.com/sogum/api/businesses?start=1&display=110&query=%EA%B0%95%EB%82%A8%EA%B5%AC%20%EA%B3%A0%EC%96%91%EC%9D%B4%EC%B9%B4%ED%8E%98&deviceType=pc',headers=headers)

    json = data.json()
    cafes = json['items']
    basic_url = 'https://store.naver.com/attractions/detail?id='
    basic_map_url = 'https://map.naver.com/v5/entry/place/'
    for cafe in cafes:
        url = basic_url + cafe['id']
        map_url = basic_map_url + cafe['id']
        address = cafe['roadAddr']
        name = cafe['name']
        price = cafe['desc']
        image = cafe['imageSrc']
        blogNum = cafe['blogCafeReviewCount']

        doc = {
            'url' : url,
            'name' : name,
            'price' : price,
            'image' : image,
            'blogNum' : blogNum,
            'mapUrl' : map_url,
            'address' : address
        }

        db.GangNam.insert_one(doc)
        print('완료!', name)

get_GangNam()