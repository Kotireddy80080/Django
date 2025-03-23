from django.contrib import admin
from application1.models import reporter
from application1.models import article
class reporter_admin(admin.ModelAdmin):
    list_display=['first_name','last_name','username','p1','p2','email']
admin.site.register(reporter,reporter_admin)

class article_admin(admin.ModelAdmin):
    list_display=['headline','public_date','reporter']
admin.site.register(article,article_admin)