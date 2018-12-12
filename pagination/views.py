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
        # GET 방식으로 전송된 파라미터 꺼내기
        page = request.GET['page']
    # 파라미터가 존재하지 않는 경우 에러 처리
    except MultiValueDictKeyError as e:
        pass
    # Board 모델로부터 글 번호 역순으로 모든 데이터 가져오기
    board_list = Board.objects.order_by('-id')
    # 데이터를 10개씩 분할
    paginator = Paginator(board_list, 10)
    # 분할된 객체 중 한개만 선정 (요청된 페이지 번호에 해당하는 객체)
    page_info = paginator.page(page)

    return render(
        request,
        'pagination/list.html',
        { 'page_info': page_info }
    )

def list2(request):
    page = '1'
    try:
        page = request.GET['page']
    except MultiValueDictKeyError as e:
        pass
    board_list = Board.objects.order_by('-id')
    paginator = Paginator(board_list, 10)
    page_info = paginator.page(page)

    start_page = (int(page) - 1) // 10 * 10 + 1
    end_page = start_page + 10

    page_list = range(start_page, end_page)

    return render(
        request,
        'pagination/list2.html',
        {
            'page_info': page_info,
            'page_list': page_list
        }
    )




