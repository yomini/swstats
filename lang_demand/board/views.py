from django.shortcuts import render
from .models import Board
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def BoardList(request):
    blist = Board.objects.all().order_by('id')
    return render(request, 'board/list.html', {'bl': blist})


def BoardWrite(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')

    elif request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        writer = request.POST['writer']
        pwd = request.POST['pwd']
        b = Board(
            title=title,
            content=content,
            writer=writer,
            pwd=pwd,
            writeDate=datetime.today()
        )
        result = b.save()
        print('=' * 60)
        print(result)

        return HttpResponseRedirect(reverse('board:board_list'))


def BoardView(request, board_id):
    bview = Board.objects.get(id=board_id)
    return render(request, 'board/view.html', {'b': bview})




