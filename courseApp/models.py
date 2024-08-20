from django.db import models
import uuid

class Course(models.Model):
    courseId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    courseCode = models.CharField(max_length=20, unique=True, blank=True)
    courseName = models.CharField(max_length=100)
    courseDescription = models.TextField()
    courseVideo = models.FileField(upload_to='videos/', null=True, blank=True)
    courseFile = models.FileField(upload_to='files/', null=True, blank=True)
    number_of_hours = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courseName

    def save(self, *args, **kwargs):
        if not self.courseCode:
            # Generate a unique course code
            self.courseCode = f'CRS{uuid.uuid4().hex[:6].upper()}'
        super().save(*args, **kwargs)
