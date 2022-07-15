from django.urls import path, include
from .auth_controller import Login

urlpatterns = [
	#path('users/',include('api.v1.modules.mobile.user.urls')),
	path('auth/login',Login.as_view()),
	path('categories/',include('api.v1.modules.mobile.category.urls')),
	path('posts/',include('api.v1.modules.mobile.post.urls')),
	path('feedbacks/',include('api.v1.modules.mobile.feedback.urls')),
	path('locations/',include('api.v1.modules.mobile.location.urls')),
	
]