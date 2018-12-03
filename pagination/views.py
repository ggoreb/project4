from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from pagination.models import Board


def insert(request):
    for i in range(1, 1001):
        Board.objects.create(
            title='제목' + str(i),
            content='내용' + str(i)
        )
    return HttpResponse('insert')

def list(request):
    page = '1'

    try:
        page = request.GET['page']
    # page = request.GET.get('page')
    except MultiValueDictKeyError as e:
        # page = '1'
        pass

    board_list = Board.objects.order_by('-id')
    paginator = Paginator(board_list, 10)
    page_info = paginator.page(page)

    return render(
        request,
        'pagination/list.html',
        { 'page_info': page_info }
    )






