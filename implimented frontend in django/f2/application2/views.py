from django.shortcuts import render
from django.views import View
class test_case1(View):
    def get(self,request):
        return render(request,"application2/s2.html")
