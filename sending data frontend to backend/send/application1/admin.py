from django.contrib import admin
from application1.models import student
class student_admin(admin.ModelAdmin):
    list_display=['sid','sname','subjects','marks','total']
admin.site.register(student,student_admin)
