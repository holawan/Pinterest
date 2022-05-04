from django.db import models
from django.contrib.auth.models import User

from projectapp.models import Project
# Create your models here.
class Article(models.Model) :
    # set_null 설정을 함으로 삭제되었을 때도 게시글이 사라지지 않고, 알 수 없음 표시가 되게 함.
    # related_name= 'article'은 유저가 여러 글을 쓸 수 있기 때문에 user가 쓴 글을 다 보려고 설정하는 것 
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='article',null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to = 'article/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

