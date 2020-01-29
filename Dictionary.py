import requests
from bs4 import BeautifulSoup


def get_dhtml(url):
    _dhtml = ""
    dresp = requests.get(url)
    if dresp.status_code == 200:
        _dhtml = dresp.text
    return _dhtml


def get_deng(code):
    schCode = code
    URL = (
        "https://search.naver.com/search.naver?where=webkr&sm=tab_jum&query=" + schCode)
    dhtml = get_dhtml(URL)
    dsoup = BeautifulSoup(dhtml, 'html.parser')
    delement = dsoup.find_all('li', class_='sh_web_top')[0]
    delement = delement.get_text()

    return delement
