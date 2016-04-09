
from student.models import Student
from django.contrib import admin

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','first_name','last_name','conceptjson')


