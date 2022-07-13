from django.shortcuts import get_object_or_404, render
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
from projectapp.models import Project
from subscribeapp.models import Subscription
@method_decorator(login_required,'get')
# youtube에서 구독을 누르면 구독버튼만 바뀐다. 
# 처리하고 바로 redirect하도록 redirectView를 사용한다
class SubscriptionView(RedirectView) :

    # 되돌아갈 곳은 project 내부 detail에서 구독을 누르는데, project_pk를 get으로 받아서 그 페이지로 되돌아감
    def get_redirect_url(self, *args, **kwargs) :
        return reverse('projectapp:detail',kwargs={'pk':self.request.GET.get('project_pk')})

    def get(self,request,*args, **kwargs) :

        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        
        subscription = Subscription.objects.filter(user=user,project=project)

        # 해당 구독정보가 존재하면 구독 취소 
        if subscription.exists() :
            subscription.delete()
        # 구독정보가 없으면 구독에 추가 
        else :
            Subscription(user=user,project=project).save()

        return super(SubscriptionView,self).get(request,*args, **kwargs)

    