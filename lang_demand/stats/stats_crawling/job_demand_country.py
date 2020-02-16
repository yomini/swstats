import urllib
from bs4 import BeautifulSoup
import urllib.request as req
import json
import re  # 숫자만 추출
from selenium import webdriver
import time


country_code = {}
with open('../../../data/country_code.json', 'r') as r:
    country_code = json.load(r)
# print(country_code)


# glassdoor에서 국가별 코드, 공고수 가져와서 json 저장
def country_web_save():
    for c in country_code.items():  # country_code 딕셔너리를 하나씩 튜플 형태로 가져옴 -> c[0]: 국가명, c[1]: 국가코드
        time.sleep(1)
        c = list(c)  # 튜플을 리스트로 바꾸기
        url = 'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=true&clickSource=searchBtn&typedKeyword=software+&sc.keyword=Software+Engineer&locT=N&locId='+c[1]+'&jobType='
        req_url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        requrl = str(urllib.request.urlopen(req_url).read())
        soup = BeautifulSoup(requrl, "html.parser")

        # software Engineer, country로 나온 공고물 개수 구하기
        if soup.select_one("#MainColSummary > p").string[0] == '0':  # 공백기준으로 나누기
            pass
        else:
            Demand = soup.select_one("#MainColSummary > p").string.split()  # 공백기준으로 나누기
            if Demand[0].find(',') >= 0:  # 콤마있으면 제거
                Demand = Demand[0].split(',')  # 숫자부분에서 쉼표기준으로 나누기
                Demand = int(Demand[0] + Demand[1])  # 숫자 합치기
            else:
                Demand = int(Demand[0])
            # print("Demand = %d" % Demand)
            country_code[c[0]] = [c[1], Demand]  # json에 {국가명: [코드, 공고수]}로 저장
            # print(country_code)
    # glassdoor의 국가코드 json 파일로 저장
    with open('../../../data\\country_code.json', 'w', encoding='UTF-8') as f:
        json.dump(country_code, f, indent='\t')


# glassdoor에서 국가별 평균연봉 가져와서 raw data 를 country_code.json에 저장
def ave_salary():
    for c in country_code.items():  # country_code 딕셔너리를 하나씩 튜플 형태로 가져옴 -> c[0]: 국가명, c[1]: 국가코드
        time.sleep(1)
        c = list(c)  # 수정을 위해 튜플을 리스트로 바꾸기
        # print(country_code)
        url = 'https://www.glassdoor.com/Salaries/company-salaries.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=software+engineer&sc.keyword=software+engineer&locT=N&locId='+c[1][0]+'&jobType='
        print(url)
        req_url = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        requrl = str(urllib.request.urlopen(req_url).read())
        soup = BeautifulSoup(requrl, "html.parser")
        # print(soup)

        # software Engineer, country로 나온 공고물 개수 구하기
        avg_s = soup.select_one(".occMedianModule__OccMedianBasePayStyle__payNumber").string.strip()
        print(avg_s)
        country_code[c[0]][2] = avg_s  #json에 value리스트에 추가
    # glassdoor의 국가코드 json 파일로 저장
    with open('../../../data\\country_code.json', 'w', encoding='UTF-8') as f:
        json.dump(country_code, f, indent='\t')


# country_code.json에 저장해놓은 raw data of salary 정제하기
sal = []  # 연봉리스트
def sal_refine():
    for c in country_code.items():  # 값들을 튜플로 가져옴
        c = list(c)  # 수정을 위해 튜플을 리스트로 바꾸기
        sal = c[1][2] # 편의를 위해 연봉을 변수에 저장
        # 데이터 정제
        sal = sal.replace(" ", "")
        sal = sal.replace(",", "")
        if sal[-1] == "K":
            sal = sal.replace("K", "000")
        sals = re.findall("\d+", sal)  # re 라이브러리 - 숫자만 추출 - 따로따로 있으면 리스트로 생성되므로 그것도 정제
        # if len(sals) >1:
        sal = sals[-1]
        if c[0] == "Korea":  #정제
            sal = sal[1:]
        print(sal)

        # json에 변수 추가
        country_code[c[0]][3] = sal  # json에 value리스트에 추가 - 딕셔너리[키값].append(추가할변수)

    # glassdoor의 국가코드 json 파일로 저장
    with open('../../../data\\country_code.json', 'w', encoding='UTF-8') as f:
        json.dump(country_code, f, indent='\t')



# 각국의 평균 연봉을 달러로 통일시키기
def change_curr():
    for c in country_code.items():
        c = list(c)  # 수정을 위해 튜플을 리스트로 바꾸기
        sal = c[1][3]  # 연봉
        cur = c[1][4]  # 화폐단위
        url = 'https://www.xe.com/currencyconverter/convert/?Amount='+sal+'&From='+cur+'&To=USD'
        # print(url)

        # 웹접속하여 달러로 변환된 연봉 변수에 저장 javascript로 동적생성되기때문에 beautifulsoup으로 html가져오듯이 하긴 어려움 -> selenium으로 쉽게
        path = 'D:\Downloads\chromedriver\chromedriver_win32\chromedriver.exe'  #셀리니움사용을 위한 크롬드라이버. 패스 지정해줘야함
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(path, chrome_options=options)
        driver.get(url)
        driver.implicitly_wait(3)  # 오류 방지
        converted_sal = driver.find_element_by_class_name('converterresult-toAmount').text

        # 연봉정보 정제, 정수로 변환
        converted_sal = converted_sal[:converted_sal.index('.')]  # 소수점제거
        converted_sal = converted_sal.replace(",", "")
        converted_sal = round(int(converted_sal), -2)  # 두번째에서 반올림
        print(converted_sal)
        driver.quit()

        # json에 저장
        country_code[c[0]][4] = converted_sal  #json에 value리스트에 추가
        with open('../../../data\\country_code.json', 'w', encoding='UTF-8') as f:
            json.dump(country_code, f, indent='\t')


# 데이터 업데이트 할 때 실행
# country_web_save()  # glassdoor에서 국가별 software engineer 공고개수 가져오기
# ave_salary()  # glassdoor에서 국가별 평균연봉 가져와서 raw data 를 country_code.json에 value에 [2] 저장
# sal_refine()  # ave_salary()에서 저장해놓은 연봉 데이터 정제하여 json에 value에 [3]번째에 저장
# change_curr()  # json value [3]번쨰  - 각국의 평균 연봉을 달러로 통일시키기 - 가져와서 [4]번째에 저장

# print(country_code)
