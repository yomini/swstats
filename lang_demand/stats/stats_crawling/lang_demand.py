import operator
import urllib
import urllib.parse
from bs4 import BeautifulSoup
import urllib.request as req
import pickle
import json
import time
# go lang 검색어, c 검색어 수정!!!!!!!!!!!!!!!!!!


#  'HTTP Error 403 : Forbidden' 에러 :
# 서버에서 사람이 아닌 자동으로 내용을 읽는 Spider/Bot 으로 판단하여 차단
# 아래와 같이 headers를 설정하여 User-Agent 를 지정해주면 실행이 된다.

langlist = {}  # {언어, 공고개수} 담을 리스트
# lang = ['java', 'javascript', 'python', 'php', 'c', 'c++', 'c%23', 'ruby', 'swift', 'golang', 'sql', 'css', 'scala', 'html', 'elixir', 'objective-c', 'kotlin', 'rust', 'f%23', 'clojure']
# data 폴더 밑에 lang_top20.json 파일을 불러와서 top 20를 dict으로 저장한다.
langdict = {}
lang = []
with open('../../../data/lang_top20.json', 'r') as r:
    langdict = json.load(r)
# 저장한 dict에서 value 값을 lang 변수에 append
lang_val_list = list(langdict.values())
for i in lang_val_list:
    lang.append(i)
file = '.html'


# glassdoor에서 소스 읽어와서 html파일로 저장 (실시간으로 읽어오면 속도가 느리므로 필요할때만 함수 호출해서 파일 저장)
def lang_save():
    global file
    for l in lang:
        time.sleep(0.5)
        # url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=' + l + '&sc.keyword=' + l + '&locT=&locId=&jobType='
        pageurl = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=%s&sc.keyword=%s&locT=&locId=&jobType=' % (urllib.parse.quote(l), urllib.parse.quote(l))
        req = urllib.request.Request(pageurl, headers={'User-Agent': 'Mozilla/5.0'})
        requrl = str(urllib.request.urlopen(req).read())
        file_name = l + file
        with open("../../../data/lang_demand_files/"+file_name, "wt") as f:
            f.write(requrl)


# html파일 읽어서 데이터 크롤링 - for문돌려서 각자 파일에서 공고개수 뽑아오기
def lang_list():
    global file, lang
    for l in lang:
        file_name = "../../../data/lang_demand_files/" + l + file
        content = open(file_name, 'rt', encoding='utf-8').read()
        soup = BeautifulSoup(content, "html.parser")
        # print(soup)

        # java라고 검색해서 나온 구인공고물 개수 구하기
        langDemand = soup.select_one("#MainColSummary > p").string.split()  # 공백기준으로 나누기
        if langDemand[0].find(',') >= 0:  # 콤마있으면 제거
            langDemand = langDemand[0].split(',')  # 숫자부분에서 쉼표기준으로 나누기
            langDemand = int(langDemand[0] + langDemand[1])  # 숫자 합치기
        else:
            langDemand = int(langDemand[0])
        # print(langDemand)
        if l.find("%") >= 0:  # f%23 -> f#으로 바꾸기
            l = l.split("%")
            l = l[0] + "#"
        langlist[l] = langDemand  # 딕셔너리에서 l 이 key고 거기에 value로 langdemand 저장
        # print(langlist)
        file_name = file
    langs = dict(sorted(langlist.items(), key=lambda item:item[1], reverse=True))  # 딕셔너리 값 기준 내림차순 정렬
    langs = {key:val for key, val in langs.items() if val > 2000}
    print(langs)
    with open('../../../data/lang_demand.json', 'w', encoding='UTF-8') as f:
        json.dump(langs, f, indent='\t')
    # dict_file = open("../../../data/lang_demand_dict.json", "wb", encoding='UTF-8')  # 딕셔너리형태의 파일로 저장 (서버 속도 개선 위함) / write+byte
    # pickle.dump(langs, dict_file)
    # dict_file.close()


# 데이터 업데이트 할 때 실행
# lang_save()
lang_list()
