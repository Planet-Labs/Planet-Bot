import requests
from bs4 import BeautifulSoup


def get_whtml(url):
    _whtml = ""
    wresp = requests.get(url)
    if wresp.status_code == 200:
        _whtml = wresp.text
    return _whtml


def get_weather(code):
    schCode = code
    URL = ("https://search.naver.com/search.naver?where=nexearch&query=" + schCode)
    whtml = get_whtml(URL)
    wsoup = BeautifulSoup(whtml, 'html.parser')
    welement = wsoup.find_all('p')
    welement1 = welement[21].get_text()
    welement2 = welement[22].get_text()
    welement = welement1 + " " + welement2
    welement = welement.replace("도씨", "")
    return welement
