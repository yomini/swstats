from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


def vote(request):
    question = get_object_or_404(Question)
    selected_choice = question.choice_set.get(id=request.POST['ch'])  # 사용자가 선택한 답html에서 name='ch'로 넘겨줘서 받은값
    selected_choice.votes += 1
    selected_choice.save()
    return render(request, 'polls/vote.html', {'q': question})


def list(request):
    qs = Question.objects.all()
    return render(request, 'polls/list.html', {'qs': qs})


