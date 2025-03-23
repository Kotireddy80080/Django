from django.contrib import admin
from application1.models import employees
class employees_class(admin.ModelAdmin):
    list_display=['first_name','last_name','username','p1','p2','email']
admin.site.register(employees,employees_class)