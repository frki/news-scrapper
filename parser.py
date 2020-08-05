"""Arg parser for scrapping (swedish) news paper"""

import argparse

from omni import omni
from nwt import nwt

url_dct = {'omni': 'https://omni.se', 'nwt': 'https://www.nwt.se'}

def parser():
    # Create top-level parser
    parser = argparse.ArgumentParser(prog='news_scrapper', description='Scrap news papper')
    parser.add_argument('-debug', action='store_true', help='Enable debug')
    subparsers = parser.add_subparsers(title="commands", dest="command", help='sub-command', required=True)

    # Create parser for omni
    parser_omni = subparsers.add_parser('omni', help='https://omni.se',
                                           description='Scrap news from https://omni.se')
    # parser_omni.add_argument('url', default='https://omni.se')
    parser_omni.add_argument('--section', default='', choices=['tech', 'inrikes', 'utrikes'],
                                help='sub-section')
    parser_omni.set_defaults(func=omni)

    # Create parser for nwt
    parser_nwt = subparsers.add_parser('nwt', help='https://www.nwt.se/',
                                           description='Scrap news from https://www.nwt.se/')
    parser_nwt.add_argument('--section', default='', choices=['nyheter', 'karlstadsliv'],
                             help='sub-section')
    parser_nwt.set_defaults(func=nwt)

    args = parser.parse_args()
    setattr(args, 'url', url_dct[args.command])
    # print(args)
    return args
