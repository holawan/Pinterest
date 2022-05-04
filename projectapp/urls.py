from django.urls import path,include

from projectapp.views import ProjectListView,ProjectCreateView,ProjectDetailView
#앱 내에 urls.py 추가 생성해주기! 
app_name = 'projectapp'
urlpatterns = [
    path('list/',ProjectListView.as_view(),name='list'),

    path('create/',ProjectCreateView.as_view(),name='create'),
    path('detail/<int:pk>/',ProjectDetailView.as_view(),name='detail')

]
