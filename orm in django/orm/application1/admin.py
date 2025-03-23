from django.contrib import admin
from application1.models import users
class users_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','p1','p2','mobile_number','email']
admin.site.register(users,users_admin)
