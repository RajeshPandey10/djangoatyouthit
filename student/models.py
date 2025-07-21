from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, blank=False, default='abcd')
    faculty = models.CharField(max_length=20, blank=False, default='abc')

    def __str__(self):
        return self.name
