from django.db import models
from django.conf import settings

class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=CASCADE, related_name='to_question')
    answer = models.TextField()
    student = models.ForeignKey('Student', on_delete=CASCADE, related_name='by_student')
    answered_on = models.DateField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)
