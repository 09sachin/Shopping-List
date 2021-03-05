from django.contrib import admin
from . models import Shopping_list
# Register your models here.


class shopping(admin.ModelAdmin):
    list_display = ('person','item_name','item_status','item_quantity','date')
    ordering = ['date']


admin.site.register(Shopping_list,shopping)