from django.contrib import admin
from .models import (
    Student, Course, Department, Lecturer, CourseRegistrationAndResult, StudentGrade
)

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Lecturer)
admin.site.register(CourseRegistrationAndResult)
admin.site.register(StudentGrade)