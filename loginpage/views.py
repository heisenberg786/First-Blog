from django.shortcuts import render
from django.http import  HttpResponse
from . import forms
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'loginpage/base.html')
def contact(request):
    return render(request,'loginpage/contact.html')
def aboutme(request):
    return render(request,'loginpage/aboutme.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registerd = False
    form = forms.UserForm()
    user_profile = forms.UserProfileForm()
    if request.method == 'POST':
        form = forms.UserForm(data=request.POST)
        user_profile = forms.UserProfileForm(data=request.POST)
        if form.is_valid() and user_profile.is_valid():
            user_form = form.save(commit=True)
            user_form.set_password(user_form.password)
            user_form.save()
            profile = user_profile.save(commit=False)
            profile.user_form = user_form
            # humlog jb upload pr click krnge image ke liye toh request bhejega kdr store krna hai image if 'Profile_pic' in request.FILES:
            #badme  profile.profile_pic = request.FILES['Profile_pic'] ye profile.profile_pic jb request krenge image ye directory se dikha dega

            if 'Profile_pic' in request.FILES:
                profile.Profile_pic = request.FILES['Profile_pic']
            profile.save()


            registerd = True

        else:
            print(form.errors,user_profile.errors)
    else:
        form = forms.UserForm()
        user_profile = forms.UserProfileForm()

        # return HttpResponse("SignUp Here!!")
    return render(request,'loginpage/register.html',{'signup_page':form,'registerd':registerd,'user_profile':user_profile})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_form = authenticate(username=username,password=password)
        if user_form:
            if user_form.is_active:
                login(request,user_form)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("<h1>You ned to register first this account does'nt belongs to anybody</h1>")
        else:
            return HttpResponse("<div class='container'> <h1>You need to register first this account does'nt belongs to anybody</h1></div>")
    else:
        return render(request,'loginpage/login.html')
