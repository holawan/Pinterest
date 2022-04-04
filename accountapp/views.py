from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld
# Create your views here.


# 브라우저에서 경로로 접속할 때, Hello world를 출력하는 view 만들기
#HTML을 가져오는게 아니라 직접 응답을 만들어서 되돌려주는 형태
# def hello_world(request) :
#     return HttpResponse('Hello world!')

def hello_world(request) :
    # get 요청을 받으면 get METHOD를 표시 
    if request.method == "POST" : 
        # request 의 post 중에서 hello_world_input 데이터를 가져오고 tmp에 넣어라
        temp = request.POST.get('hello_world_input')
        # DB를 구성한 모델을 가져온다. 

        
        new_hello_world = HelloWorld()
        #POST로 받아온 값을 DB에 추가해준다.
        #new_hello_world 인스턴스의 text에 temp를 저장 
        new_hello_world.text = temp
        new_hello_world.save()

        return render(request,'accountapp/hello_world.html',context={'hello_world_output': new_hello_world})
    # POST 요청을 받으면 POST MEHTOD 표시 
    else :
        return render(request,'accountapp/hello_world.html',context={'text': 'GET METHOD'})

