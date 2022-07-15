from dataclasses import field, fields
from multiprocessing import context
from django.shortcuts import render,redirect
from rest_framework import generics
from modules.posts.models import *
from api.v1.modules.serializers.mobile.category_serializer import *
from api.v1.modules.response_handler import response_handler
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.conf import settings
from django.contrib import messages
from django.db import models
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt

class PostListView(ListView):
    model =  Post
    template_name = 'post_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()        
        return context

class CreatePostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    locations = Location.objects.all()
    categories = Category.objects.all()
    fields = ['heading','category','description','user','location','mobile']
    success_url = '/admin/post-add'    
    def get_context_data(self, **kwargs):        
        context = super().get_context_data(**kwargs)
        user = self.request.user
        #pdb.set_trace()
        context['posts'] = Post.objects.all()
        context['categories'] = Category.objects.all()
        
        return context