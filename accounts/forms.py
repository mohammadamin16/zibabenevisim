from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from kavenegar import *


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=40)
    display_name = forms.CharField(max_length=140)
    phone = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput())
    username.label = 'نام کاربری'
    display_name.label = 'نامی که نمایش داده میشود'
    phone.label = 'موبایل'
    password.label = 'رمز عبور'

    def save_user(self):
        get_user_model().objects.create_user(
            self.cleaned_data['phone'],
            self.cleaned_data['username'],
            self.cleaned_data['display_name'],
            self.cleaned_data['password']
        )
        api = KavenegarAPI('64667A6443417761774762323331612B69433976514155622F52615A727A764541733555637A7A484E54453D')
        msg = 'Hi {}. Your Account Has been created successfully'.format(self.cleaned_data['display_name'])
        params = {'sender': '1000596446', 'receptor': self.cleaned_data['phone'], 'message': msg}
        response = api.sms_send(params)

