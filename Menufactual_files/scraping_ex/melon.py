import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
res = requests.get('https://www.melon.com/chart/index.htm', headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

ranks = soup.select('#lst50 > td:nth-child(2) > div > span.rank')
songs = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
singer = soup.select('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank02 > a')

leng = len(ranks)
with open('melon.txt', 'w', encoding='utf-8') as f:
    for i in range(0, leng):
        f.write(ranks[i].text.strip() + '/' + songs[i].text.strip() + '/' + singer[i].text.strip() + '\n')