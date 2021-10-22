from django.db import models
from django.conf import settings

class Quiz(models.Model):
    title = models.CharField(max-length=128)
    created_by = models.ForeignKey('Instructor', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    finished_by = models.ManyToManyField('Student', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    type = models.CharField(max-length=64)
    description = models.TextField()

    def __str__(self):
        return f'{self.type}: {self.description}'

class Choice(models.Model):
    choice = models.CharField(max-length=256)

    def __str__(self):
        return self.choice
