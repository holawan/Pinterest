from articleapp.models import Article
from django.http import HttpResponseForbidden
def article_ownership_required(func) :
    def decorated(request,*args, **kwargs) :
        # 요청을 받으면서 받은 pk를 pk로 가지고 있는 articleobject
        article = Article.objects.get(pk=kwargs['pk'])
        #글쓴이가 요청한 유저가 아니면 404 
        if not article.writer == request.user :
            return HttpResponseForbidden()
        return func(request,*args,**kwargs)
    return decorated