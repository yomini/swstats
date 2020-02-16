from django.contrib import admin
from .models import *  # import할때 주소 동일하면 제거해야됨...인식안됨...


# admin페이지 관리 - Choice테이블을 Question 테이블 안에 넣기 (두 테이블을 한 화면에 보이게. inline기능)
class ChoiceInline(admin.StackedInline):  # 인라인 (Question섹션 안에 Choice 섹션 넣기. 두개의 테이블을 하나의 화면에 보이게 해줌)하기위해 admin에 StackedInline상속받음
    model = Choice
    extra = 2  # Choice 모델을 2번 넣어준다.


# admin페이지 관리 - Question 테이블의 필드 관리
class QuestionAdmin(admin.ModelAdmin):  # 필드 관리하려면 admin에 ModelAdmin상속

    inlines = [ChoiceInline]  # Choice모델넣어주는 함수를 배열로 하나씩 가져옴

    # Question섹션에 보이는 필드 순서 변경
    # fields = ['pub_date', 'question_text']

    # 필드 분리
    fieldsets = [('question', {'fields': ['question_text']}),
                 ('date', {'fields': ['pub_date']})
                 ]

    #  필드 접기
    # fieldsets = [('question', {'fields': ['question_text']}),
    #              ('date', {'fields': ['pub_date'], 'classes':['collapse']})
    #              ]


# ***********************************************
# * 관리자페이지에 보여줄 테이블에 관한 함수 추가  *
# ***********************************************
admin.site.register(Question, QuestionAdmin)  # Question테이블, Question필드관리테이블
admin.site.register(Choice)  # Choice테이블
