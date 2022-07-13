from django.contrib import admin

from articleapp.models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin) :
    list_display=('pk','writer','title')


admin.site.register(Article,ArticleAdmin)