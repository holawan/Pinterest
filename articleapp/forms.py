from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm) :

    class Meta :
        model = Article
        #writer은 서버 내부에서 설정한다. 
        fields = ['title','image','project','content']