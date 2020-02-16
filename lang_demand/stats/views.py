from django.shortcuts import render
from .stats_crawling.lang_visual import *
from .stats_crawling.salary_visual import sal_vis


# # 언어별 수요 그래프 가져와서 html에 넘기기


def language(request):
    langvi = langvis()
    salvi = sal_vis()
    return render(request, 'stats/language.html', {'lv': langvi, 's':salvi})  # template 생략