from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_course, name='add_course'),
    path('update/<int:course_id>/', views.update_course, name='update_course'),
    # path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
      path('delete/<int:course_id>/', views.delete_course, name='delete_course'),
    path('find/name/<str:name>/', views.find_course_by_name, name='find_course_by_name'),
    path('find/course_code/<str:code>/', views.find_course_by_code, name='find_course_by_course_code'),
    path('courses/', views.display_courses, name='display_courses'),
    path('count/', views.number_of_courses, name='number_of_courses'),
]
