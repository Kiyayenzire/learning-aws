from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('my-login', views.my_login, name='my-login'),
    path('profile-management', views.profile_management, name='profile-management'),
    path('user-logout', views.user_logout, name='user-logout'),
    path('dlete-account', views.delete_account, name='delete-account'),
      
]

