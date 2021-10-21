from django.db import models
from django.conf import settings

# from api.models import Course

class Quiz(models.Model):
    title = models.CharField(max-length=128)
    created_by = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=modles.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    finished_by = models.ManyToManyField('Student')

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    type = models.CharField(max-length=64)
    description = models.TextField()

class MultipleChoice(Question):
    pass

class TextAnswer(Question):
    pass
