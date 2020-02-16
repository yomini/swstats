# 프로그래밍 언어의 순위를 json파일로 저장하는 처리

# 컴퓨터 언어 순위 - https://www.tiobe.com/tiobe-index
# JSON 형식으로 저장한다.
from bs4 import BeautifulSoup as bs
import urllib.request as req
import json

# https://www.tiobe.com/documentation/ -> TIOBE Index : Top 20 Programming Language
url = 'https://www.tiobe.com/tiobe-index/'
res = req.urlopen(url)

# 데이터 불러오기
soup = bs(res, 'lxml')
# print(soup)

# Top 20 데이터 추출하기
table = soup.select('table#top20 > tbody > tr')
# print(table)

# 저장할 dict 변수 선언
lang_top20 = {}
# key가 될 변수 ( 1~20 )
cnt = 1
for dataes in table:
    data = dataes.select('td')
    data_str = str(data[3].string)
    # /가 있으면 ' '으로 대체
    if data_str.find('/') >= 0:
        data_str = data_str.replace('/', ' ')
        lang_top20[str(cnt)] = data_str
    elif data_str.find('/') < 0:
        lang_top20[str(cnt)] = data_str
    cnt += 1
print("최종", lang_top20)

# json 데이터로 저장한다.
with open('../../../data\\lang_top20.json', 'w', encoding='UTF-8') as f:
    json.dump(lang_top20, f, indent='\t')




