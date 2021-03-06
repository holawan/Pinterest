#acount 내부에서 url을 사용하도록 내부에 urls.py를 만들어줌 ! 프로젝트 urls.py에서 연동됨 
from accountapp import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView

#앱네임과 path에 name을 설정해주면 name을 입력했을 때 path로 자동 이동해주는 역할을 할 수 있다.
app_name = 'accountapp'
urlpatterns = [
    # login, logoutview 만들기
    path('login/',LoginView.as_view(template_name="accountapp/login.html"),name = 'login'),
    path('logout/', LogoutView.as_view(),name='logout'),

    path('create/',views.AccountCreateView.as_view(),name='create'),
    path('detail/<int:pk>/',views.AccountDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.AccountUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.AccountDeleteView.as_view(),name='delete'),
    # path('text_delete/<int:pk>/',views.text_delete,name='text_delete'),
]
