from django.shortcuts import render,redirect
from api.models import Posts,UserProfile
from django.contrib.auth.models import User
from postweb.forms import SignUpForm,LogInForm,ProfileForm
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=SignUpForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        print("post1")
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            print("inside")
            return redirect("login")
        else:
            print("outside")
            return render(request,"signup.html",{"form":form})


class LogInView(View):
    def get(self,request,*args,**kwargs):
        form=LogInForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LogInForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})

class HomeView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"home.html")

class ProfileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=ProfileForm()
        return render(request,"profile_create.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=ProfileForm(request.POST,files=request.FILES)
        if form.is_valid():
            usr=User.objects.get(username=request.user.username)
            form.instance.user=usr
            form.save()
            # print(request.FILES)
            # print(request.user)
            # print(form.cleaned_data)
            # usr=User.objects.get(username=request.user.username)
            # UserProfile.objects.create(**form.cleaned_data,user=usr)
            return redirect("profile_detail")
        else:
            return render(request,"profile_create.html",{"form":form})

class ProfileView(View):
    def get(self,request,*args,**kwargs):
        qs=UserProfile.objects.filter(user=request.user)
        return render(request,"profile.html",{"profile":qs})