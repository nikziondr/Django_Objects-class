from django.contrib import admin
from .models import School, Faculty, Student, Certificate_type, Department, Grade
# Register your models here.

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Certificate_type)
admin.site.register(Department)
admin.site.register(Grade)