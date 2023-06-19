from django.contrib import admin
from .models import Course, Teacher, Student, Test

# Register your models here.

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Test)
