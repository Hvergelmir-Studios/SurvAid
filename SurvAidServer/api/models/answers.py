from django.db import models
from django.conf import settings

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=CASCADE)
    answer = models.TextField()
    student = models.ForeignKey('Student', on_delete=CASCADE)
    answered_on = models.DateField(auto_now_add=True)
    is_correct = BooleanField(default=False)
