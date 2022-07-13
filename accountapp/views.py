# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountUpdateForm

from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article


has_ownership = [account_ownership_required,login_required]



# 장고의 크리에이트 뷰 상속 받기 
class AccountCreateView(CreateView) :
    #파라미터 1 무슨 모델 ?
    model = User
    # 계정은 중요한 과정이기 때문에 기본적 템플릿을 제공한다.
    form_class = UserCreationForm
    # 계정을 만들 때 성공했으면 경로 지정 
    # reverse_lazy는 
    success_url = reverse_lazy('articleapp:list')
    # 회원가입 할 때 볼 HTML 지정 
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView,MultipleObjectMixin) :
    model = User 
    # target_user를 설정하지 않으면 
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs) :
        object_list = Article.objects.filter(writer = self.get_object ()) 
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)

# 클래스에 데코레이터를 적용할 수 있는 method_decorator
@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')

class AccountUpdateView(UpdateView) :
    #파라미터 1 무슨 모델 ?
    model = User
    # 계정은 중요한 과정이기 때문에 기본적 템플릿을 제공한다.
    form_class = AccountUpdateForm
    # 계정을 만들 때 성공했으면 경로 지정 
    # reverse_lazy는 
    success_url = reverse_lazy('articleapp:list')
    # 정보수정할 때  할 때 볼 HTML 지정 
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'

@method_decorator(has_ownership,'get')
@method_decorator(has_ownership,'post')

class AccountDeleteView(DeleteView) :
    model = User 
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
