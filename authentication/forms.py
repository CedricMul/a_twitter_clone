from django import forms
from twitteruser.models import MyTwitterUser

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = MyTwitterUser
        fields = [
            'username',
            'password'
        ]

class SignInForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(widget=forms.PasswordInput)
