from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class test_case1(View):
    def get(self,request):
       return HttpResponse("<center><h1><tt>class compount</tt></h1></center>")
