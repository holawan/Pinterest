from django.contrib import admin

from profileapp.models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin) :
    list_display=('pk','user','nickname')


admin.site.register(Profile,ProfileAdmin)