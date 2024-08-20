from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Course
from .serializers import CourseSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_course(request):
    parser_classes = (MultiPartParser, FormParser)
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_course(request, course_id):
    parser_classes = (MultiPartParser, FormParser)
    course = get_object_or_404(Course, id=course_id)
    serializer = CourseSerializer(course, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    course.delete()
    return Response({'message': 'Course deleted successfully'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_course_by_name(request, name):
    course = get_object_or_404(Course, name=name)
    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def find_course_by_code(request, code):
    course = get_object_or_404(Course, code=code)
    serializer = CourseSerializer(course)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def display_courses(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def number_of_courses(request):
    count = Course.objects.count()
    return Response({'number_of_courses': count}, status=status.HTTP_200_OK)
