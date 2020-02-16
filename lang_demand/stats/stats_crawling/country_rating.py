# Top 10 국가 + 한국과 국가별 glassdoor의 코드를 json파일로 저장하는 처리

# Top 10 countries for Software engineers / Developers/ Data Scientists to work
# https://www.hackerearth.com/blog/developers/best-countries-software-engineers-developers-work-2017/
# 더 최신의 데이터나 신뢰할 수 있는 사이트를 찾는다면 데이터를 바꾼다
# Top 10 국가를 JSON 형식의 데이터로 저장한다. + Korea 추가
from bs4 import BeautifulSoup as bs
import urllib.request as req
import json

# 데이터가 있는 URL Open
url = 'https://www.hackerearth.com/blog/developers/best-countries-software-engineers-developers-work-2017/'
res = req.urlopen(url)

# 데이터 불러오기
soup = bs(res, 'lxml')
# print(soup.prettify())

div = soup.find('div', {'class': 'entry-content'})
country_list = div.select('strong')

# key가 될 변수 선언
key = 1
# dict로 저장할 변수 선언
country_top10 = {}
for c in country_list:
    country_top10[str(key)] = c.string
    key += 1
    print(country_top10)

country_top10['11'] = 'Korea'
print('최종', country_top10)

# data 폴더에 country_top10.json으로 저장
with open('../../../data/country_top10.json', 'w', encoding='UTF-8') as f:
    json.dump(country_top10, f, indent='\t')

# Switzerland - 226, Canada - 3, Australia - 16, Netherlands - 178, Germany - 96, USA - 1, Sweden - 223,
# Denmark - 63, Singapore - 271, United Kingdom - 2, South Korea - 135
# glassdoor의 국가코드 저장
country_top10 = {}
with open('../../../data\\country_top10.json', 'r', encoding='UTF-8') as r:
    country_top10 = json.load(r)
print(country_top10)

# top 10 국가가 저장된 리스트
top10_country = list(country_top10.values())
# 국가별 코드가 저장된 리스트
top10_code = ['226', '3', '16', '178', '96', '1', '223', '63', '271', '2', '135']
# 국가코드 저장할 dict 변수
country_code = {}
cnt = 0
for i in range(0, 11):
    country_code[top10_country[i]] = top10_code[i]

print('최종', country_code)

# glassdoor의 국가코드 json 파일로 저장
with open('../../../data\\country_code.json', 'w', encoding='UTF-8') as f:
    json.dump(country_code, f, indent='\t')
