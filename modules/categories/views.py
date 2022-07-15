from dataclasses import field, fields
from multiprocessing import context
from django.shortcuts import render,redirect
from rest_framework import generics
from modules.categories.models import *
from api.v1.modules.serializers.mobile.category_serializer import *
from api.v1.modules.response_handler import response_handler
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from modules.categories.models import *
from django.conf import settings
from django.contrib import messages
from django.db import models
from rest_framework.permissions import IsAdminUser
from django.views.decorators.csrf import csrf_exempt

import pdb
# Create your views here.
class CategoryListView(ListView):
    model =  Category
    template_name = 'category_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = Category.objects.all()        
        return context

class CreateCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ['category_name','category_image','parent_category',]
    success_url = '/admin/category-list'    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['categories'] = Category.objects.all()
        return context

class UpdateCategoryView(UpdateView):   
    model = Category
    template_name = 'update_category.html'
    fields = ['category_name','category_image','parent_category',]
    success_url = '/admin/category-list'
    def update(self, request, pk):        
        query_obj =  self.get_object()
        return query_obj


def CategoryDeleteView(request,pk):   
    category = Category.objects.get(id=pk) 
    category.delete()    
    return redirect('/admin/category-list')