# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Product,Mood,Talk

# Register your models here.

admin.site.register(Post)
admin.site.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display=('nickname', 'message','pub_time')
    ordering=('-pub_time',)
admin.site.register(Mood)
admin.site.register(Talk, PostAdmin)
