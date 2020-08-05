"""scrap Omni"""

import requests
from bs4 import BeautifulSoup as bs4


def omni(url, section):
    """Scrap Omni news paper, https://omni.se'"""
    if section:
        section = '/' + section
    # print(f"Got url: {url}{section}")
    res = requests.get(url + section)
    soup = bs4(res.text, 'html.parser')
    print(f"News from: {soup.title.text}\n")
    hrefs = soup.find_all('a', {'class': 'article-link'})
    for href in hrefs:
        link = url + href['href']
        txt = href.find('h1').text.strip()
        print(f"{txt} [{link}]")
