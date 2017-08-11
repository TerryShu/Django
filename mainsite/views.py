# -*- coding: utf-8 -*-
from django.template.loader import get_template
import random
from django.http import HttpResponse , Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Post, Product
from datetime import datetime


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


def listing(request):
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset='utf-8'>
    <title>Product</title>
    </head>
    <body>
    <table widyh=400 border=1 bgcolor='#ccffcc'>
    {}
    </table>
    </body>
    </html>
    '''

    product = Product.objects.all()
    tags = '<tr><td>項目</td><td>大小</td><td>數量</td></tr>'
    for p in product:
        tags = tags + '<tr><td>{}</td>'.format(p.title)
        tags = tags + '<td>{}</td>'.format(p.size)
        tags = tags + '<td>{}</td></tr>'.format(p.num)

    return HttpResponse(html.format(tags))

def about(request):
    template = get_template('about.html')
    quotes = ['1','2','3','4','5']
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)

def disp_detail(request , sku):
    try:
        p = Product.objects.get(id = sku)
    except Product.DoesNotExist:
        raise Http404("Not Found!!")


    template = get_template('dispdetail.html')
    html = template.render({'product': p})
    return HttpResponse(html)

def show_time(request):
    template = get_template('nowtime.html')
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

