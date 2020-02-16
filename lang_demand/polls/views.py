from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


# views.py : 화면에 보이는 내용

# 컨트롤러와 같은 기능
# request요청이 들어오면 polls/index.html 띄워라.


def index(request):
    return render(request, 'polls/index.html')
    # 요청을 가지고 가서 polls/list.html 실행해라.
    # 계속 타고타고 온거 합치면 http://127.0.0.1:8000/polls/ 로 입력하면 index.html 함수 실행 (templates는 생략되는 이유: html 은 항상 templates 아래애 있는 걸로 인식됨)


def test(request):
    # 삽입: save()
    # q = Question(question_text='What is your favorite color?: ', pub_date='2020-01-27')  # 객체 생성
    # q.save()

    # 수정: save()
    # q = Question(id=2, question_text='What is your favorite sports?: ', pub_date='2020-01-27')  # 2번째 id(오라클에서는 sequence개념)의 내용을 수정하겠다.
    # q.save()

    # 조회 (select * 과 같은 개념)
    # qlist = Question.objects.all().order_by('question_text')
    # print(type(qlist))
    # for q in qlist:
    #     print(q.question_text, q.pub_date)

    # 삭제 .get은 한개만, .all은 전부 다 가져오기
    q = Question.objects.get(id=2)
    q.delete()
    return render(request, 'polls/test.html')


def insert(request):
    # q = Question(question_text='What is your favorite TV show?: ', pub_date='2020-01-28')
    # q.save()

    # q = Question(question_text='What is your favorite movie star?: ', pub_date='2020-01-28')
    # q.save()

    # q = Question(question_text='What is your hobby?: ', pub_date='2020-01-28')
    # q.save()

    # q = Question(question_text='What is your favorite food?: ', pub_date='2020-01-28')
    # q.save()

    # # q = Question(question_text='What is your favorite brand?: ', pub_date='2020-01-28')
    # # q.save()

    return render(request, 'polls/insert.html')


# 질문목록 보여주기
def list(request):
    qs = Question.objects.all()
    return render(request, 'polls/list.html', {'qs': qs})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'q': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = question.choice_set.get(id=request.POST['ch'])  # 사용자가 선택한 답html에서 name='ch'로 넘겨줘서 받은값
    selected_choice.votes += 1
    selected_choice.save()
    return render(request, 'polls/vote.html', {'q': question})
