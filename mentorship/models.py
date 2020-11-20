from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    courses = models.TextField()
    teacher = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return self.first_name + ' ' + self.last_name