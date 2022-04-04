from django.db import models

# Create your models here.
# models에서 Model(기초적인 모델)을 상속 받음 
class HelloWorld(models.Model) :

    text = models.CharField(max_length=255,null = False)