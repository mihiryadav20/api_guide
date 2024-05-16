from django.db import models

# Create your models here.
class Student(models.Model):
    stuname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.stuname

