# studentApp/views.py

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from courseApp.models import Course
from paypack.client import HttpClient
from paypack.transactions import Transaction
from django.db import IntegrityError
from rest_framework.decorators import api_view, permission_classes

# Initialize Paypack Client
client_id = "4889551c-3078-11ef-a1c1-deade826d28d"
client_secret = "16e130bab1d09ffd96dc41be30981a8eda39a3ee5e6b4b0d3255bfef95601890afd80709"
HttpClient(client_id=client_id, client_secret=client_secret)

@csrf_exempt
@api_view(['POST'])
def create_student(request):
        
        amount = request.data.get('amount')
        phone = request.data.get('phone')

        # Check if amount and phone are provided
        if not amount or not phone:
            return JsonResponse({'error': 'Amount and phone number are required'}, status=400)

        try:
            # Convert amount to integer
            amount = float(amount)
        except ValueError:
            return JsonResponse({'error': 'Invalid amount'}, status=400)

        cashin = Transaction().cashin(amount=amount, phone_number=phone)
        print(f'\n\n Status: {cashin} \n\n')
        
        if cashin.get('status') == 'success':
            status = 'approved'
        else:
            status = 'denied'

        student = Student.objects.create(
            firstname=request.data.get('firstname'),
            lastname=request.data.get('lastname'),
            phone=phone,
            user_id=request.data.get('user_id'),
            course_id=request.data.get('course_id'),
            status=status
        ) 
        return JsonResponse({'id': student.id, 'status': student.status})




@csrf_exempt
def update_student(request, student_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=student_id)
        data = request.POST
        amount = data.get('amount')
        phone = data.get('phone')

        cashin = Transaction().cashin(amount=amount, phone_number=phone)

        if cashin.get('status') == 'success':
            student.status = 'approved'
        else:
            student.status = 'denied'

        student.firstname = data.get('firstname', student.firstname)
        student.lastname = data.get('lastname', student.lastname)
        student.phone = phone
        student.user_id = data.get('user_id', student.user_id)
        student.course_id = data.get('course_id', student.course_id)
        student.save()

        return JsonResponse({'id': student.id, 'status': student.status})

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Other views...
def get_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return JsonResponse({
        'id': student.id,
        'firstname': student.firstname,
        'lastname': student.lastname,
        'phone': student.phone,
        'status': student.status,
        'created_date': student.created_date,
    })

def get_students_by_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    data = [{'id': student.id, 'firstname': student.firstname, 'lastname': student.lastname, 'status': student.status} for student in students]
    return JsonResponse(data, safe=False)

def get_students_by_status(request, status):
    students = Student.objects.filter(status=status)
    data = [{'id': student.id, 'firstname': student.firstname, 'lastname': student.lastname, 'status': student.status} for student in students]
    return JsonResponse(data, safe=False)

def get_students_by_firstname(request, firstname):
    students = Student.objects.filter(firstname__icontains=firstname)
    data = [{'id': student.id, 'firstname': student.firstname, 'lastname': student.lastname, 'status': student.status} for student in students]
    return JsonResponse(data, safe=False)

def get_students_by_lastname(request, lastname):
    students = Student.objects.filter(lastname__icontains=lastname)
    data = [{'id': student.id, 'firstname': student.firstname, 'lastname': student.lastname, 'status': student.status} for student in students]
    return JsonResponse(data, safe=False)

def get_student_by_phone(request, phone):
    student = get_object_or_404(Student, phone=phone)
    return JsonResponse({
        'id': student.id,
        'firstname': student.firstname,
        'lastname': student.lastname,
        'phone': student.phone,
        'status': student.status,
        'created_date': student.created_date,
    })
