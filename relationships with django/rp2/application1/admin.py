from django.contrib import admin
from application1.models import products
from application1.models import customers
class products_admin(admin.ModelAdmin):
    list_display=['pid','pname','price','company','m_date','e_date']
admin.site.register(products,products_admin)

class customers_admin(admin.ModelAdmin):
    list_display=['cid','cname','address','mobile','email']
admin.site.register(customers,customers_admin)
