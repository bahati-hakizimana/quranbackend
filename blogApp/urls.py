# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.get_all_blogs, name='get_all_blogs'),
    path('blog/<int:blog_id>/', views.get_blog_by_id, name='get_blog_by_id'),
    path('blog/title/<str:title>/', views.get_blog_by_title, name='get_blog_by_title'),
    path('add/', views.create_blog, name='create_blog'),
    path('update/<int:blog_id>/', views.update_blog, name='update_blog'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete_blog'),
    path('count/', views.count_blogs, name='count_blogs'),
]
