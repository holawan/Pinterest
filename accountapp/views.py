# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm
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

        # 경로를 다시 만들어주려면 reverse라는 함수를 써야한다. 
        #어카운트에 헬로우 월드로 재접속하라 ?
        return redirect(reverse('accountapp:hello_world'))
    # POST 요청을 받으면 POST MEHTOD 표시 
    else :
        hello_world_list = HelloWorld.objects.all()[::-1]
        return render(request,'accountapp/hello_world.html',context={'hello_world_list': hello_world_list})

# 장고의 크리에이트 뷰 상속 받기 
class AccountCreateView(CreateView) :
    #파라미터 1 무슨 모델 ?
    model = User
    # 계정은 중요한 과정이기 때문에 기본적 템플릿을 제공한다.
    form_class = UserCreationForm
    # 계정을 만들 때 성공했으면 경로 지정 
    # reverse_lazy는 
    success_url = reverse_lazy('accountapp:hello_world')
    # 회원가입 할 때 볼 HTML 지정 
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView) :
    model = User 
    # target_user를 설정하지 않으면 
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# update view는 createview와 거의 유사하다.
class AccountUpdateView(UpdateView) :
    #파라미터 1 무슨 모델 ?
    model = User
    # 계정은 중요한 과정이기 때문에 기본적 템플릿을 제공한다.
    form_class = AccountUpdateForm
    # 계정을 만들 때 성공했으면 경로 지정 
    # reverse_lazy는 
    success_url = reverse_lazy('accountapp:hello_world')
    # 정보수정할 때  할 때 볼 HTML 지정 
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView) :
    model = User 
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'