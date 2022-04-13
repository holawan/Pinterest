from .models import Profile
from django.http import HttpResponseForbidden


def profile_ownership_required(func) :
    def decorated(request,*args, **kwargs) :
        
        profile = Profile.objects.get(pk=kwargs['pk'])
        #요청을 보낸 유저와 profileuser가 같지 않다면 forbidden 리턴 
        if profile.user != request.user :
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated