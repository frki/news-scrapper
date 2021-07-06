"""scrap Omni"""

import requests
from bs4 import BeautifulSoup as bs4
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
c_handler = logging.StreamHandler()
logger.addHandler(c_handler)


def omni(url, section, debug):
    """Scrap Omni news paper, https://omni.se'"""
    if debug:
        logger.setLevel(logging.DEBUG)
    if section:
        section = '/' + section
    logger.debug(f"Fetching url: {url}{section}")
    res = requests.get(url + section)
    soup = bs4(res.text, 'html.parser')
    print(f"Omni News (section: {soup.title.text})\n")
    hrefs = soup.find_all('a', {'class': 'article-link'})
    logger.debug(f'hrefs: {hrefs}s')
    for href in hrefs:
        link = url + href['href']
        txt = href.find('h1').text.strip()
        logger.info(f"{txt} [{link}]")
