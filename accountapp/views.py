from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# 브라우저에서 경로로 접속할 때, Hello world를 출력하는 view 만들기
def hello_world(request) :
    return HttpResponse('Hello world!')

