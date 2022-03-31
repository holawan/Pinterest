from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# 브라우저에서 경로로 접속할 때, Hello world를 출력하는 view 만들기
#HTML을 가져오는게 아니라 직접 응답을 만들어서 되돌려주는 형태
# def hello_world(request) :
#     return HttpResponse('Hello world!')

def hello_world(request) :
    return render(request,'base.html')

