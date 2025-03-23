from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
class test_case1(View):
    def get(self,request):
       return HttpResponse('<h1><tt>welcome to django</tt></h1>')
