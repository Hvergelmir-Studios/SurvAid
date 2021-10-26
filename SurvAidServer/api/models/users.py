from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_instructor = models.BooleanField()

    def __str__(self):
        if is_instructor:
            status = 'Instructor'
        else:
            status = 'Student'

        return f'{status}: {self.get_full_name()}, {self.get_username()}'

class Instructor(User):
    is_instructor = models.BooleanField(default=True)

class Student(User):
    is_instructor = models.BooleanField(default=False)
