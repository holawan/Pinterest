from django.contrib import admin

from subscribeapp.models import Subscription

# Register your models here.


class SubscriptionAdmin(admin.ModelAdmin) :
    list_display=('pk','user','project')


admin.site.register(Subscription,SubscriptionAdmin)