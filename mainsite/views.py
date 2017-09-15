# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.template.loader import get_template
import random
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from datetime import datetime
from .models import Post, Product, Mood, Talk
from datetime import datetime
from django.template import RequestContext, Context, Template
from django.shortcuts import render
from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from mainsite import form
from django.core.mail import EmailMessage

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
    quotes = ['1', '2', '3', '4', '5']
    html = template.render({'quote': random.choice(quotes)})
    return HttpResponse(html)


def disp_detail(request, sku):
    try:
        p = Product.objects.get(id=sku)
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


def show_try(request, year, month, day):
    sum1 = int(year) + int(month) + int(day)
    template = get_template('try.html')
    html = template.render(locals())
    return HttpResponse(html.format(sum1))


def tvshow(request, num='0'):
    tv_list = [{'name': '不曾回來過', 'tvcode': 'bpJko9n8KTY'},
               {'name': '魚仔', 'tvcode': 'ybfWYpYhTQQ'},
               {'name': '飄向北方', 'tvcode': 'qIF8xvSA0Gw'},
               {'name': '不在聯繫', 'tvcode': 'hgPBTs7_0js'}, ]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    minu = now.timetuple().tm_min
    template = get_template('tv.html')
    tvnum = num
    tv = tv_list[int(tvnum)]
    html = template.render(locals())
    return HttpResponse(html)


def FBLogin(request):
    template = get_template('FBtry.html')
    html = template.render(locals())
    return HttpResponse(html)


'''def talkget(request, pid=None, del_pass=None):
    template = get_template('talk.html')
    posts = Talk.objects.order_by('-pub_time')[:30]
    moods = Mood.objects.all()

    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要張貼訊息，則每一個欄位都要填...'

    if del_pass and pid:
        try:
            post = Talk.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "資料刪除成功"
            else:
                message = "密碼錯誤"
    elif user_id != None:
        mood = Mood.objects.get(status=user_mood)
        post = Talk.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存！'.format(user_pass)

    html = template.render(locals())

    return HttpResponse(html)'''


def talk(request):
    template = get_template('talk.html')
    moods = Mood.objects.all()
    ctx = {}
    ctx.update(csrf(request))
    message = '如要張貼訊息，則每一個欄位都要填...'
    if 'ok' in request.POST:
        user_id = request.POST['user_id']
        user_pass = request.POST['user_pass']
        user_post = request.POST['user_post']
        user_mood = request.POST['mood']
        mood = Mood.objects.get(status=user_mood)
        post = Talk.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功儲存！'

    return render(request, "talk.html", locals())


def talklist(request):
    template = get_template('talklist.html')
    posts = Talk.objects.order_by('-pub_time')[:30]
    html = template.render(locals())
    return HttpResponse(html)


def mail(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.method == 'POST':
        forms = form.ContactForm(request.POST)
        if forms.is_valid():
            message = "感謝您的來信，我們會儘速處理您的寶貴意見。"
            user_name = forms.cleaned_data['user_name']
            user_city = forms.cleaned_data['user_city']
            user_email = forms.cleaned_data['user_email']
            user_message = forms.cleaned_data['user_message']

            mail_body = u'''
        網友姓名：{}
        居住城市：{}
        反應意見：如下
        {}'''.format(user_name, user_city, user_message)

            email = EmailMessage('來自myweb',
                                 mail_body,
                                 user_email,
                                 ['wind850101@gmail.com'])
            email.send()
        else:
            message = '請檢查輸入是否正確'
    else:
        forms = form.ContactForm()

    return render(request, "mail.html", locals())

def diary(request):
    ctx = {}
    ctx.update(csrf(request))
    if request.method == 'POST':
        login_form = form.DairyLogin(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['name']
            user_color = login_form.cleaned_data['color']
            message = 'sucess'
        else:
            message = 'fail'
    else:
        login_form = form.DairyLogin()

    response = render(request,"diary.html",locals())
    try:
        if user_name: response.set_cookie('username',user_name)
        if user_color: response.set_cookie('usercolor',user_color)
    except:
        pass

    return response