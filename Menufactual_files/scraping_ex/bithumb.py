import requests
from bs4 import BeautifulSoup

# 1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장
req = requests.get('https://www.bithumb.com').text

# 2. 정보를 조작하기 편하게 바꾸고,
soup = BeautifulSoup(req, 'html.parser')

# 3. 바꾼 정보 중 원하는 것만 뽑아서, 출력한다.
# kospi = soup.select_one('#tableAsset > tbody > tr:nth-child(1) > td:nth-child(1) > p > a')
#assetRealBTC
name_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(1) > p > a > strong')
money_tags = soup.select('#tableAsset > tbody > tr > td:nth-child(2) > strong')

# for name_tag in name_tags:
#     print(name_tag.text.strip())

leng = len(money_tags)
with open("bithumb.txt", "w", encoding = 'utf-8') as f:
    for i in range(0, leng):
        f.write(name_tags[i].text.strip() + '/ ' + money_tags[i].text.strip() + '\n')