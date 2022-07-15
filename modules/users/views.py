#from msilib.schema import ListView
from django.shortcuts import render, redirect
from modules.users.models import *
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages 
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
import pdb
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/admin/dashboard')
        else:
            return render(request,'login.html')       
    return render(request,'login.html')

class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['latest_articles'] = Article.objects.all()[:5]
        return context

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()        
        return context

def CreateUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        user = User.objects.create(first_name=first_name,last_name=last_name,email=email)
        user.save()
        profile = UserProfile.objects.create(user=user,mobile=mobile)        
        return redirect('/admin/user-list')
    return render(request,'add_user.html')
    