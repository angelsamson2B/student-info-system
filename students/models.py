from django.db import models

# Create your models here.
class Student(models.Model):
    student_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    address = models.TextField()
    birthdate = models.DateField()
    contact_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.student_number})"