from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_exam, name='add_exam'),
    path('', views.display_exams, name='display_exams'),
    path('course_code/<str:course_code>/', views.find_exam_by_course_code, name='find_exam_by_course_code'),
    path('course_name/<str:course_name>/', views.find_exam_by_course_name, name='find_exam_by_course_name'),
    path('id/<int:exam_id>/', views.find_exam_by_id, name='find_exam_by_id'),
    path('update/<int:exam_id>/', views.update_exam, name='update_exam'),
    path('delete/<int:exam_id>/', views.delete_exam, name='delete_exam'),
    path('add_question/<int:exam_id>/', views.add_question, name='add_question'),
    path('update_question/<int:question_id>/', views.update_question, name='update_question'),
    path('delete_question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('search_question/<str:search_question>/', views.search_question, name='search_question'),
    path('number_of_exams/', views.number_of_exams, name='number_of_exams'),
    path('number_of_questions/', views.number_of_questions, name='number_of_questions'),
    path('number_of_questions_in_exam/<int:exam_id>/', views.number_of_questions_in_exam, name='number_of_questions_in_exam'),
]
