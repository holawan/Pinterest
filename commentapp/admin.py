from django.contrib import admin

from commentapp.models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin) :
    list_display=('pk','article','writer')


admin.site.register(Comment,CommentAdmin)