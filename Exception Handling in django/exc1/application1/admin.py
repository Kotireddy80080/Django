from django.contrib import admin
from application1.models import products1
class product_admin(admin.ModelAdmin):
    list_display=['id','pid','pname','price','company','m_date','e_date']
admin.site.register(products1,product_admin)
