from django.urls import path
from . import views
from .views import PostListView, PostDetialView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
    path('', PostListView.as_view(), name="blog_home"),
 	path('post/<int:pk>/', PostDetialView.as_view(), name="post_details"),
 	path('post/new/', PostCreateView.as_view(), name="post_create"),
 	path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
 	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('about_us/', views.about_us, name="blog_about"),
    
]
