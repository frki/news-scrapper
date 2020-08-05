"""Scrap NWT"""

import re

import requests
from bs4 import BeautifulSoup as bs4


def nwt(url, section):
    """Scrap NWT news paper, https://www.nwt.se"""
    # TODO
    if section:
        section = '/' + section
    # print(f"Got url: {url}{section}")
    res = requests.get(url + section)
    soup = bs4(res.text, 'html.parser')
    print(f"News from: {soup.title.text}\n")
    if not section:
        hrefs = soup.find_all('a', {'class': 'articles-list__link'})
    else:
        # regex = re.compile('.*karlstadsliv')  # TODO: did fail
        regex = re.compile('.*')
        hrefs = soup.find_all('a', {'title': regex})
    # print(hrefs)
    for href in hrefs:
        link = href['href']
        txt = href['title']
        if "NWT Media AB" in txt:  # removing link if exist
            continue
        print(f"{txt} [{link}]")
