import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_ihtml(url):
    _ihtml = ""
    iresp = requests.get(url)
    if iresp.status_code == 200:
        _ihtml = iresp.text
    return _ihtml


def get_image(code):
    schCode = code
    URL = ("https://search.naver.com/search.naver?where=kin&query=" + schCode + "+-일본어로+-중국어로+-영어로")
    ihtml = get_ihtml(URL)
    isoup = BeautifulSoup(ihtml, 'html.parser')
    ielement = isoup.find_all('dt', class_='question')[0].get_text() + "\n" + isoup.find_all('dd', class_='answer')[0].get_text()


    return ielement

