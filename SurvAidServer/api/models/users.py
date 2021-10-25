from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    

class Instructor(User):
    pass

class Student(User):
    pass
