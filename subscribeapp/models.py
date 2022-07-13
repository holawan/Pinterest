from django.db import models
from django.contrib.auth.models import User
from projectapp.models import Project 
# Create your models here.
class Subscription(models.Model) :

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name='subscription')

    class Meta :
        # user와 project의 쌍은 오직 하나만 ! 
        unique_together = ('user', 'project')

    def __str__(self):
        return self.project.title
    