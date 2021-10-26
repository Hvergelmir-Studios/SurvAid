from rest_framework import serializers
from .models import *

class AnswerSerializer(serializers.ModelSerializer):

    class meta:
        model = Answer
        fields = (
            'question',
            'answer',
            'student',
            'answered_on',
            'is_correct')
