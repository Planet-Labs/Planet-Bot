import requests
from bs4 import BeautifulSoup

def get_html(url):
    _html = ""
    resp = requests.get(url)
    if resp.status_code == 200:
        _html = resp.text
    return _html


def get_song(ymd, code):
    schCode = code
    schYmd = ymd
    URL = (
            "http://music.bugs.co.kr/chart/track/day/total?chartdate=%s" % schYmd
    )
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all("tr")
    element = element[schCode].find_all('a')
    element = element[2]
    element = element.get_text()

    return element


def get_singer(ymd, code):
    schCode = code
    schYmd = ymd
    URL = (
            "http://music.bugs.co.kr/chart/track/day/total?chartdate=%s" % schYmd
    )
    html = get_html(URL)
    soup = BeautifulSoup(html, 'html.parser')
    element = soup.find_all("tr")
    element = element[schCode].find_all('a')
    element = element[3]
    element = element.get_text()

    return element
