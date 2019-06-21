import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
res = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = BeautifulSoup(res, 'html.parser')
tags = soup.select('#lst50')

with open('melon2.txt', 'w', encoding='utf-8') as f:
    for tag in tags:
        rank = tag.select_one('td:nth-child(2) > div > span.rank').text.strip()
        song = tag.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
        singer = tag.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
        f.write(f'{rank} / {song} / {singer}\n')