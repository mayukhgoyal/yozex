from django.urls import path, include
from modules.users.views import *
from modules.categories.views import *
from modules.posts.views import *
urlpatterns = [
    path('signin',signin, name="signin"),
    path('dashboard',Dashboard.as_view(), name="dashboard"),
    path('user-list',UserListView.as_view(), name="user-list"),
    path('user-add',CreateUser,name="user-add"),
    path('category-list',CategoryListView.as_view(), name="category-list"),
    path('category-add',CreateCategoryView.as_view(), name="category-add"),
    path('category/<pk>/update',UpdateCategoryView.as_view(), name="category-update"),
    path('category/<pk>/delete',CategoryDeleteView,name="category-delete"),
    path('post-list',PostListView.as_view(), name="post-list"),
    path('post-add',CreatePostView.as_view(), name="post-list"),
]