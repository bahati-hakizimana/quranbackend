from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Exam, Question
from courseApp.models import Course
from userApp.models import CustomUser

class ExamTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user and authenticate
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword', email='test123@gmail.com')
        self.client.login(username='testuser', password='testpassword')
        self.course = Course.objects.create(code="CS101", name="Computer Science", description="CS Course", number_of_hours=50)
        self.exam = Exam.objects.create(course=self.course, created_at='2023-01-01')

    def test_add_exam(self):
        data = {'course': self.course.id, 'created_at': '2023-06-01'}
        response = self.client.post(reverse('add_exam'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_display_exams(self):
        url = reverse('display_exams')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_find_exam_by_code(self):
        url = reverse('find_exam_by_code', args=['CS101'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_find_exam_by_course_name(self):
        url = reverse('find_exam_by_course_name', args=['Computer Science'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_find_exam_by_id(self):
        url = reverse('find_exam_by_id', args=[self.exam.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.exam.id)

    def test_update_exam(self):
        url = reverse('update_exam', args=[self.exam.id])
        data = {
            'course': self.course.id  # Assuming you want to update the course or some other field
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.exam.refresh_from_db()
        # Add assertions if other fields are updated

    def test_delete_exam(self):
        url = reverse('delete_exam', args=[self.exam.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Exam.objects.filter(id=self.exam.id).exists())

    def test_add_question(self):
        url = reverse('add_question', args=[self.exam.id])
        data = {
            'question': 'What is Django?',
            'answer': 'A web framework',
            'marks': 10
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_question(self):
        self.question = Question.objects.create(exam=self.exam, question="What is AI?", answer="Artificial Intelligence", marks=10)
        url = reverse('update_question', args=[self.question.id])
        data = {
            'question': 'What is REST?',
            'answer': 'Representational State Transfer',
            'marks': 15
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.question.refresh_from_db()
        self.assertEqual(self.question.question, 'What is REST?')
        self.assertEqual(self.question.answer, 'Representational State Transfer')
        self.assertEqual(self.question.marks, 15)

    def test_delete_question(self):
        self.question = Question.objects.create(exam=self.exam, question="What is AI?", answer="Artificial Intelligence", marks=10)
        url = reverse('delete_question', args=[self.question.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Question.objects.filter(id=self.question.id).exists())

    def test_search_question(self):
        self.question = Question.objects.create(exam=self.exam, question="What is AI?", answer="Artificial Intelligence", marks=10)
        url = reverse('search_question', args=['AI'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

    def test_number_of_exams(self):
        url = reverse('number_of_exams')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number_of_exams'], Exam.objects.count())

    def test_number_of_questions(self):
        url = reverse('number_of_questions')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number_of_questions'], Question.objects.count())

    def test_number_of_questions_in_exam(self):
        self.question = Question.objects.create(exam=self.exam, question="What is AI?", answer="Artificial Intelligence", marks=10)
        url = reverse('number_of_questions_in_exam', args=[self.exam.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['number_of_questions'], self.exam.questions.count())
