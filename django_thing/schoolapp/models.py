from django.db import models
from datetime import datetime

# Create your models here.

class School(models.Model):
    school_name = models.CharField(max_length=400)

    def __str__(self):
        return self.school_name


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=400)

    def __str__(self):
        return self.faculty_name

class Certificate_type(models.Model):
    cert_name = models.CharField(max_length=400)

    def __str__(self):
        return self.cert_name

class Department(models.Model):
    dept_name = models.CharField(max_length=400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.dept_name

class Grade(models.Model):
    grade_type = models.CharField(max_length=400)

class Student(models.Model):
    full_name = models.CharField(max_length=400)
    grad_year = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    cert_type = models.ForeignKey(Certificate_type, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

