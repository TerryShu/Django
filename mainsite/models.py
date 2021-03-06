# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


# Create your models here.



class Post(models.Model):
    bool = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    my_date = models.DateField(auto_now=True)
    upload = models.FileField(upload_to='uploads/%Y%m%d', default=False)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title


class Product(models.Model):
    SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    title = models.CharField(max_length=200)
    size = models.CharField(max_length=1, choices=SIZE, default='M')
    num = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title


class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return self.status


class Talk(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default='匿名者')
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20, null = False)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=20, null = False)

    def __unicode__(self):
        return self.name
