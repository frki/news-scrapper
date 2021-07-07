"""Scrap DN"""

import re

import requests
from bs4 import BeautifulSoup as bs4
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
c_handler = logging.StreamHandler()
logger.addHandler(c_handler)


def dn(url, section, debug):
    """Scrap DN news paper, https://www.dn.se"""
    if debug:
        logger.setLevel(logging.DEBUG)
    if section:
        section = '/' + section
    logger.debug(f"Fetching url: {url}{section}")
    res = requests.get(url + section)
    soup = bs4(res.text, 'html.parser')
    logger.info(f"DN News (section: {soup.title.text.strip()})\n")

    hrefs = soup.find_all('a', {'class': 'teaser'})
    logger.debug(f'first href:{hrefs[0]}')

    for href in hrefs:
        link = url + href['href']
        try:
            txt = href.h1.text.strip()
        except AttributeError:
            continue  # ignonre 'h2'

        logger.info(f"{txt} [{link}]")
