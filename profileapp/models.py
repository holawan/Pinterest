from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model) :
    # profile 주인이 누군지 일대일 매칭 
    # on_delete의 역할은 객체가 사라질 때 이 프로필도 없어지게 하려고 CASCADE 설정 
    #따라서 유저가 사라질 때 삭제됨 
    # related_name설정하면 user.profile 같은 식으로 profile에 접근할 수 있다 
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')

    # 이미지가 업로드 되었을 때 서버내부에 저장될 곳을 정해주는 경로  upload_to
    # null은 ture로 설정해서 프로필 사진을 올리지 않아도 괜찮게 만듬  
    image = models.ImageField(upload_to='profile/',null=True)

    # 닉네임은 유일한 닉네임을 가지도록 unique= True로 함 
    nickname = models.CharField(max_length = 20, unique=True, null=True)

    #대화명
    message = models.CharField(max_length=100, null =True)

    