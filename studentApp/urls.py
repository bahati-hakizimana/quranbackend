
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student, name='create_student'),
    path('update/<int:student_id>/', views.update_student, name='update_student'),
    path('<int:student_id>/', views.get_student_by_id, name='get_student_by_id'),
    path('course/<int:course_id>/', views.get_students_by_course, name='get_students_by_course'),
    path('status/<str:status>/', views.get_students_by_status, name='get_students_by_status'),
    path('firstname/<str:firstname>/', views.get_students_by_firstname, name='get_students_by_firstname'),
    path('lastname/<str:lastname>/', views.get_students_by_lastname, name='get_students_by_lastname'),
    path('phone/<str:phone>/', views.get_student_by_phone, name='get_student_by_phone'),
]
