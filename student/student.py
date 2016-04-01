
from django.db import models

class Student(models.Model):
    moodle_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

