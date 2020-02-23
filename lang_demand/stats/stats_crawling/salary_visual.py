import json
import os
import pickle
import urllib
import io
import base64
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

country = []
wage_dollor = []


# 언어별 수요 막대그래프 시각화
def sal_vis():
    # x축 언어, y축 공고개수 셋팅
    # absolute_path = os.path.dirname(os.path.abspath(__file__))
    with open('D:\Workspace\MachineLearning_SW_Engineering\swstats\data\country_code.json', 'r') as r:
        country_code = json.load(r)
        # print(country_code)
    for c in country_code.items():
        country.append(c[0])
        wage_dollor.append(c[1][4])
    # print(country)
    # print(wage_dollor)

    fig = plt.figure(figsize=(10,8))
    plt.bar(country, wage_dollor, align="center", width=0.6 )
    plt.title('Software Developer Salaries in the World')
    plt.xlabel('Country')
    plt.ylabel('Salary in US$')
    plt.xticks(rotation=45)
    plt.tight_layout()  # 여백 자동 조정
    # plt.show()

    # base64로 그래프 인코딩 (html파일에서 그래프 이미지로 삽입하기 위함)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    print(uri)
    return uri


sal_vis()
