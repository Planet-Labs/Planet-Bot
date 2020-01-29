import requests
from bs4 import BeautifulSoup


def get_khtml(url):
    _khtml = ""
    kresp = requests.get(url)
    if kresp.status_code == 200:
        _khtml = kresp.text
    return _khtml


def get_knoledge(code):
    schCode = code
    URL = ("https://terms.naver.com/search.nhn?query=" + schCode + "&searchType=&dicType=&subject=")
    khtml = get_khtml(URL)
    ksoup = BeautifulSoup(khtml, 'html.parser')
    kelement = ksoup.find_all('p', class_='desc __ellipsis')
    kelement = kelement[0]
    kelement = kelement.get_text()
    return kelement
