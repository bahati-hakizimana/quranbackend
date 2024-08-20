# studentApp/models.py

from django.db import models
from django.contrib.auth import get_user_model
from courseApp.models import Course

User = get_user_model()

class Student(models.Model):
    STATUS_CHOICES = [
        ('approved', 'Approved'),
        ('denied', 'Denied')
    ]

    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='denied')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname}'
