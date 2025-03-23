from django.contrib import admin
from application1.models import place
from application1.models import hotel
from application1.models import waiters
class place_Admin(admin.ModelAdmin):
    list_display=['name','address']
admin.site.register(place,place_Admin)

class hotel_Admin(admin.ModelAdmin):
    list_display=['place']
admin.site.register(hotel,hotel_Admin)

class waiters_Admin(admin.ModelAdmin):
    list_display=['first_name','last_name','hotel']
admin.site.register(waiters,waiters_Admin)

