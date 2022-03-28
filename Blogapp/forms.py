from django import forms
from .models import Blog,ContactDetails
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,SetPasswordForm,PasswordChangeForm,PasswordResetForm,UsernameField
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation

class SignUpform(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username','email']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                    'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs= {'class' : 'form-control','autofocus':True,'strip':False}))
    password = forms.CharField(label=_("Password"),strip=False, widget=forms.PasswordInput(attrs= {'class' : 'form-control','autocomplete':'current-password','autofocus':True}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password") ,strip=False,widget=forms.PasswordInput(attrs= {'class' : 'form-control','autocomplete':'current-password','autofocus':True}))
    new_password1 = forms.CharField(label=_("New Password") ,strip=False,widget=forms.PasswordInput(attrs= {'class' : 'form-control','autocomplete':'current-password','autofocus':True}))
    new_password2 = forms.CharField(label=_("New Password Confirmation"),strip=False ,widget=forms.PasswordInput(attrs= {'class' : 'form-control','autocomplete':'current-password','autofocus':True}))

class PasswordResetForm(PasswordResetForm):
    email = forms.CharField(label=_("Email"),widget=forms.PasswordInput(attrs= {'class' : 'form-control','autocomplete':'email'}))

class PasswordResetConfirm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True}))
    new_password2 = forms.CharField(label=_("New Password Confirmation"), strip=False, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'autocomplete': 'current-password', 'autofocus': True}))

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"