# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.
class Eventadmin(admin.ModelAdmin):
    list_display = ['name','status','address','linit','start_time']
    search_fields = ['name']

class Guestadmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','create_time']
    search_fields = ['realname']
admin.site.register(Event,Eventadmin)
admin.site.register(Guest,Guestadmin)