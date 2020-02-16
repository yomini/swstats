# 언어별 각 국가의 수요 구하기
from bs4 import BeautifulSoup
import urllib.request as req
from urllib.parse import quote
import json

# 언어 가져오기
lang_dict = {}
with open('../../../data/lang_top20.json', 'r') as r:
    lang_dict = json.load(r)
lang_dict_items = lang_dict.items()
lang_list = list(lang_dict.values())

# 국가 가져오기
country_dict = {}
with open('../../../data/country_code.json', 'r') as r:
    country_dict = json.load(r)
# 국가와 코드 리스트
country_dict_items = list(country_dict.items())

# 전역변수
strL = ''
lang_country_dict = {}
countrydict = {}
demandList = []


def langDemandList():
    langlist = []  # {언어, 공고개수} 담을 리스트
    global strL
    for l in lang_list:
        if l.find('#') >= 0:
            strL = l.replace('#', '%23')
            url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn' \
                  '&typedKeyword=%s&sc.keyword=%s&locT=&locId=&jobType=' % (quote(strL), quote(strL))
        else:
            url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn' \
                  '&typedKeyword=%s&sc.keyword=%s&locT=&locId=&jobType=' % (quote(l), quote(l))
        # print(url)
        requrl = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        res = req.urlopen(requrl).read()
        soup = BeautifulSoup(res, "lxml")
        # print(soup)

        # java라고 검색해서 나온 구인공고물 개수 구하기
        langDemand = soup.select_one("#MainColSummary > p").string.split()  # 공백기준으로 나누기
        if langDemand[0].find(',') >= 0:  # 콤마있으면 제거
            langDemand = langDemand[0].split(',')  # 숫자부분에서 쉼표기준으로 나누기
            langDemand = int(langDemand[0] + langDemand[1])  # 숫자 합치기
        else:
            langDemand = int(langDemand[0])
        print(l, langDemand)
        # if l.find("%23") >= 0:
        #     l = l[0]+chr(23)
        langlist.append({l: langDemand})
    print(langlist)
    return langlist


# langDemandList()


# 미국, 캐나다, 영국, 호주 등
def countryDemandList():
    global country_dict_items, strL, countrydict, lang_country_dict
    for lk, lv in lang_dict_items:
        print('key = %s' % lk, type(lk))
        print('lang = %s' % lv, type(lv))
        if lv is 'Visual Basic .NET':
            continue
        if lk == '12':
            break
        for c in country_dict_items:
            print(c)
            if lv.find('#') >= 0:
                strL = lv.replace('#', '%23')
            else:
                strL = lv
            url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn' \
                  '&typedKeyword=%s&sc.keyword=%s&locT=N&locId=%s&jobType=' % (quote(strL), quote(strL), quote(c[1][0]))
            requrl = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            res = req.urlopen(requrl).read()
            soup = BeautifulSoup(res, "lxml")

            countryDemand = soup.select_one('#MainColSummary > p').string.split()
            print(c)
            print(countryDemand)
            # ('Germany', '96')
            # ['20,299', 'Jobs']
            # {'java': {'switzerland': xxxx, 'sss': xxx}, 'c':{'d':xxx, 'dd':sss..}.. }
            if countryDemand[0].find(',') >= 0:  # 콤마있으면 제거
                countryDemand = countryDemand[0].split(',')  # 숫자부분에서 쉼표기준으로 나누기
                countryDemand = int(countryDemand[0] + countryDemand[1])  # 숫자 합치기
            else:
                countryDemand = int(countryDemand[0])
            print(countryDemand)
            countrydict[c[0]] = countryDemand
            print(countrydict)
        lang_country_dict[lv] = countrydict
        print(lang_country_dict)
        countrydict = {}

    #     demandList.insert(-1, countrydict)
    #     lang_country_dict[l] = demandList
    #     countrydict = {}
    #     demandList = []
    #     print(lang_country_dict)
    # print('최종', lang_country_dict)
    return lang_country_dict


demanddict = countryDemandList()
with open('../../../data\\lang_country_demand.json', 'w', encoding='UTF-8') as f:
    json.dump(demanddict, f, indent='\t')

# 데이터를 추가할 경우
# with open('../../../data\\lang_country_demand.json', 'a', encoding='UTF-8') as f:
#     json.dump(demanddict, f, indent='\t')
