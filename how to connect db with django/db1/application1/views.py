from django.shortcuts import render
from django.views import View
from application1.models import students
class test_case1(View):
    def get(self,request):
        obj1=students.objects.all()
        return render(request,"application1/S1.html",{'obj1':obj1})
