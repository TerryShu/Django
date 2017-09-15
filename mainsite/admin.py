# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post,Product,Mood,Talk

# Register your models here.

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Mood)
admin.site.register(Talk)