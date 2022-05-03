from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,DetailView,UpdateView,DeleteView,ListView
from articleapp.decorator import article_ownership_required
from articleapp.forms import ArticleCreationForm
from django.utils.decorators import method_decorator
from articleapp.models import Article
from django.views.generic.edit import FormMixin

from commentapp.forms import CommentCreationForm
# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreatView(CreateView) :
    model = Article
    form_class = ArticleCreationForm 
    template_name = 'articleapp/create.html'

    def form_valid(self,form) :
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()

        return super().form_valid(form)
    def get_success_url(self) :
        return reverse('articleapp:detail',kwargs={'pk' : self.object.pk})

class ArticleDetailView(DetailView,FormMixin) :
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView) :
    model = Article
    form_class = ArticleCreationForm 
    template_name = 'articleapp/update.html'
    context_object_name = 'target_article'
    def get_success_url(self) :
        return reverse('articleapp:detail',kwargs={'pk' : self.object.pk})

@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView) :
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'

    success_url = reverse_lazy('articleapp:list')

class ArticleListView(ListView) :
    model = Article 
    context_obejct_name = 'article_list'
    template_name = 'articleapp/list.html'
    #한 페이지에 보여야 하는 객체 수 
    paginate_by = 3
