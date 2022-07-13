from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm) :

    content = forms.CharField(widget=forms.Textarea(attrs={'class' : 'editable text-left',
                                                            'style' : 'height auto;' }))
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    class Meta :
        model = Article
        #writer은 서버 내부에서 설정한다. 
        fields = ['title','image','project','content']