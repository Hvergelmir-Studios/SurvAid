from django.db import models
from django.conf import settings

class Course(models.Model):
    name = models.CharField(max-length=64)
    course_id = models.CharField(max-length=16)
    created_by = models.ForeignKey('Instructor', on-on_delete=models.CASCADE)
