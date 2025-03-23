from django.shortcuts import render
from application1.models import products
class product_koti(koti.modelAdmin):
    list_display=['id','pid','pname','price','m_date','e_date']
admin.site