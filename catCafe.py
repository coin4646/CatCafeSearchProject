import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def get_urls():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://store.naver.com/attractions/list?display=9&query=%EA%B0%95%EB%82%A8%EA%B5%AC%20%EA%B3%A0%EC%96%91%EC%9D%B4%EC%B9%B4%ED%8E%98&sessionid=SmpfOJ6KFU2yHptSuPAu0Pss&sortingOrder=precision&start=1',headers=headers)


    soup = BeautifulSoup(data.text, 'html.parser')

    cafes = soup.select('#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul > li')

    for cafe in cafes:
        title = cafe.select_one('div > div > div.tit > span > a > span').text

        print(title)
