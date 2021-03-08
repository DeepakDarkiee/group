from account import views
from django.urls import path, include
from dsgroup import urls as dsgroup_urls
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



urlpatterns = [

	path('',views.user_login,name='user_login'),
   	#path("signup/",views.register,name="reg"),
	#path("check_user/",views.check_user,name="check_user"),
	path("user_logout/",views.user_logout,name="user_logout"),
	#path("edit_profile/",views.edit_profile,name="edit_profile"),
	#path("change_password/",views.change_password,name="change_password"),
	
]


