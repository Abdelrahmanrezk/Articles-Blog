from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.user_register, name="users_register"),
  	path('profile/', views.user_profile, name="user_profile"),
]
