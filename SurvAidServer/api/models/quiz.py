from django.db import models
from django.conf import settings

# from api.models import Course

class Quiz(models.Model):
    title = models.CharField(max-length=128)
    created_by = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=modles.CASCADE)
    date_created = models.DateField()
    questions = models.ManyToManyField('Question')
    finished_by = models.ManyToManyField('Student')
