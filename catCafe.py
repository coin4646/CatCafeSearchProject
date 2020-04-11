import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta

def get_urls():
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)


    soup = BeautifulSoup(data.text, 'html.parser')

    cafes = soup.select('#container > div.placemap_area > div.list_wrapper > div > div.list_area > ul > li')

    for cafe in cafes:
        title = cafe.select_one('div > div > div.tit > span > a > span').text

        print(title)
