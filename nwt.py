"""Scrap NWT"""

import re

import requests
from bs4 import BeautifulSoup as bs4
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
c_handler = logging.StreamHandler()
logger.addHandler(c_handler)


def nwt(url, section, debug):
    """Scrap NWT news paper, https://www.nwt.se"""
    if debug:
        logger.setLevel(logging.DEBUG)
    if section:
        section = '/' + section
    logger.debug(f"Fetching url: {url}{section}")
    res = requests.get(url + section)
    soup = bs4(res.text, 'html.parser')
    logger.info(f"NWT News (section: {soup.title.text})\n")
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
        logger.info(f"{txt} [{link}]")
