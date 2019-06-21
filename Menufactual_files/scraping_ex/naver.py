import requests
from bs4 import BeautifulSoup

# 1. 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장
req = requests.get('https://www.naver.com').text

# 2. 정보를 조작하기 편하게 바꾸고,
soup = BeautifulSoup(req, 'html.parser')

# 3. 바꾼 정보 중 원하는 것만 뽑아서, 출력한다.
kospi = soup.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div')
print(kospi.text)

