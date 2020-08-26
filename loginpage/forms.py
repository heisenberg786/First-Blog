from django import forms
from loginpage.models import Login_page
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = Login_page
        fields = '__all__'
