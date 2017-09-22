# _*_ encoding: utf-8 *_*
from django import forms
from mainsite import models


class ContactForm(forms.Form):
    CITY = [
        ['TP', '台北'],
        ['TY', '桃園'],
        ['TC', '台中'],
        ['TN', '台南'],
        ['KS', '高雄'],
        ['NA', '其他'],
    ]
    user_name = forms.CharField(label='您的姓名', max_length=50)
    user_city = forms.ChoiceField(label='居住城市', choices=CITY)
    user_email = forms.EmailField(label='電子郵件')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)

class DairyLogin(forms.Form):
    color = [
        ['red', '紅'],
        ['orange', '橙'],
        ['yellow', '黃'],
        ['green', '綠'],
        ['blue', '藍'],
        ['light', '靛'],
        ['purple', '紫'],
    ]
    name = forms.CharField(label='您的姓名', max_length=50)
    color = forms.ChoiceField(label='幸運色',choices=color)

class Login(forms.Form):
    account = forms.CharField(label='帳號', max_length=10)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput())