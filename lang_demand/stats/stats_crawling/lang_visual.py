import json
import os
import pickle
import urllib
import matplotlib.pyplot as plt
import io
import base64

yLangs = []
xDemands = []
# 언어별 수요 막대그래프 시각화
def langvis():
    # x축 언어, y축 공고개수 셋팅
    with open('D:\Workspace\MachineLearning_SW_Engineering\swstats\data\lang_demand.json', 'r') as r:
        langd = json.load(r)
        print(langd)
    for c in langd.items():
        yLangs.append(c[0])
        xDemands.append(c[1])
    # print(yLangs)
    # print(xDemands)


    # barh: horizontal bar plot 그리기
    fig = plt.figure()
    plt.barh(yLangs, xDemands)
    plt.title('Programming Language Profession Demand')
    plt.xlabel('Job Demand')
    plt.ylabel('Language')
    # plt.show()

    # base64로 그래프 인코딩 (html파일에서 그래프 이미지로 삽입하기 위함)
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + urllib.parse.quote(string)
    print(uri)
    return uri


# langvis()
