from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['courseId', 'courseCode', 'courseName', 'courseDescription', 'courseVideo', 'courseFile', 'number_of_hours', 'total_price', 'created_date']
