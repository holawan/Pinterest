#acount 내부에서 url을 사용하도록 내부에 urls.py를 만들어줌 ! 프로젝트 urls.py에서 연동됨 
from accountapp import views
from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreatView, ArticleDetailView, ArticleListView, ArticleUpdateView,ArticleDeleteView
#앱네임과 path에 name을 설정해주면 name을 입력했을 때 path로 자동 이동해주는 역할을 할 수 있다.
app_name = 'articleapp'
urlpatterns = [
    path('list/', ArticleListView.as_view(),name='list'),
    path('create/', ArticleCreatView.as_view(),name='create'),
    path('detail/<int:pk>', ArticleDetailView.as_view(),name='detail'),
    path('update/<int:pk>', ArticleUpdateView.as_view(),name='update'),
    path('delete/<int:pk>', ArticleDeleteView.as_view(),name='delete'),
    

]
