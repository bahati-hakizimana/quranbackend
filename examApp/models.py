from django.db import models
from courseApp.models import Course

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_marks(self):
        return self.questions.aggregate(models.Sum('marks'))['marks__sum'] or 0

class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()
    answer = models.TextField()
    marks = models.IntegerField()
