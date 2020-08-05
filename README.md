# News scrapper
Scrap (swedish) news pages

_Expexted stdout_
```bash
<news title [<link>]
this is a title [https://omni.se/page/for/title]
```

## how to
1. clone repo `git clone <repo>`
2. setup environment 
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
3. run `python news_scrapper.py`

_example_
```bash
$ python news_scrapper.py -h
usage: news_scrapper [-h] [-debug] {omni} ...

Scrap news papper

optional arguments:
  -h, --help  show this help message and exit
  -debug      Enable debug

commands:
  {omni}      sub-command
    omni      https://omni.se
```

_example: sub-command_
```bash
$ python news_scrapper.py omni -h
usage: news_scrapper omni [-h] [--section {tech,inrikes,utrikes}]

Scrap news from https://omni.se

optional arguments:
  -h, --help            show this help message and exit
  --section {tech,inrikes,utrikes}
                        sub-section
```

## supported news pages
- omni
- nwt


_wish list_
- aftonbladet
- expressen
- dn
- other?
