from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Exam, Question
from courseApp.models import Course
from .serializers import ExamSerializer, QuestionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_exam(request):
    course_code = request.data.get('course_code')
    number_of_questions = request.data.get('number_of_questions')
    total_marks = request.data.get('total_marks')

    course = get_object_or_404(Course, course_code=course_code)

    exam = Exam(course=course, number_of_questions=number_of_questions, total_marks=total_marks)
    exam.save()

    return Response({'message': 'Exam created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def display_exams(request):
    exams = Exam.objects.all()
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def find_exam_by_course_code(request, course_code):
    exams = Exam.objects.filter(course__course_code=course_code)
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def find_exam_by_course_name(request, course_name):
    exams = Exam.objects.filter(course__name=course_name)
    serializer = ExamSerializer(exams, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def find_exam_by_id(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    serializer = ExamSerializer(exam)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.total_marks = request.data.get('total_marks', exam.total_marks)
    exam.save()
    return Response({'message': 'Exam updated successfully'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    exam.delete()
    return Response({'message': 'Exam deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_question(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    question = request.data.get('question')
    answer = request.data.get('answer')
    marks = request.data.get('marks')
    question = Question(exam=exam, question=question, answer=answer, marks=marks)
    question.save()
    return Response({'message': 'Question added successfully'}, status=status.HTTP_201_CREATED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.question = request.data.get('question', question.question)
    question.answer = request.data.get('answer', question.answer)
    question.marks = request.data.get('marks', question.marks)
    question.save()
    return Response({'message': 'Question updated successfully'}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return Response({'message': 'Question deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([AllowAny])
def search_question(request, search_question):
    questions = Question.objects.filter(question__icontains=search_question)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def number_of_exams(request):
    count = Exam.objects.count()
    return Response({'number_of_exams': count})

@api_view(['GET'])
@permission_classes([AllowAny])
def number_of_questions(request):
    count = Question.objects.count()
    return Response({'number_of_questions': count})

@api_view(['GET'])
@permission_classes([AllowAny])
def number_of_questions_in_exam(request, exam_id):
    exam = get_object_or_404(Exam, id=exam_id)
    count = exam.questions.count()
    return Response({'number_of_questions': count})
