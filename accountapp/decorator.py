from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
def account_ownership_required(func) :
    def decorated(request,*args, **kwargs) :
        # 요청을 받으면서 받은 pk를 pk로 가지고 있는 userobject
        user = User.objects.get(pk=kwargs['pk'])
        if user != request.user :
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated