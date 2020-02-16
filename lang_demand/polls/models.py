from django.db import models

# models.py : 데이터 연동.
# class 하나당 테이블 1개가 만들어짐
# 아래 Question, Choice가 각각 하나의 테이블.
# 장고의 model들은 무조건 (models.Model) 상속받는다...
#


class Question(models.Model):
    question_text = models.CharField(max_length=200)   # 칼럼명 = varchar(200)
    pub_date = models.DateTimeField('date published')  # 칼럼명 = date

    def __str__(self):  # java의 to_string과 동일. 이게 있어야 dto안의 리스트들이 object로 나오지 않고 text로 나온다.
        return self.question_text

    # 테이블이름 수정하기 (cmd창에서 찍어보면 테이블명 polls.Question으로 나오는 것을 polls 붙지 않고 question만 나오게 수정)
    # class Meta:
        # db_table = 'question'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 외래키 지정시 자식키가 됨. 부모글 지우면 자식글도 지워짐
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text  # JAVA의 toString()의 역할. 이게 없으면 object객체만 보여주기때문에 그 객체안의 텍스트를 가져와야함...
