import requests
import pandas as pd
from html_table_parser.parser import HTMLTableParser

html = requests.get('https://na.op.gg/summoner/champions/ajax/champions.rank/summonerId=86862704&season=15&').content
def main():
    url = 'http://www.twitter.com'
    xhtml = url_get_contents(url).decode('utf-8')

    p = HTMLTableParser()
    p.feed(xhtml)
    pprint(p.tables)

# df_list = pd.read_html(html)
# print(html)

