from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


# 브라우저에서 경로로 접속할 때, Hello world를 출력하는 view 만들기
#HTML을 가져오는게 아니라 직접 응답을 만들어서 되돌려주는 형태
# def hello_world(request) :
#     return HttpResponse('Hello world!')

def hello_world(request) :
    # get 요청을 받으면 get METHOD를 표시 
    if request.method == "POST" : 
        return render(request,'accountapp/hello_world.html',context={'text': 'POST METHOD'})
    # POST 요청을 받으면 POST MEHTOD 표시 
    else :
        return render(request,'accountapp/hello_world.html',context={'text': 'GET METHOD'})

