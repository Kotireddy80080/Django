from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
def test_case1(request):
    return HttpResponse('<center><h1><tt>service_one</center></tt></h1>')
def test_case2(request):
    return HttpResponse('<center><h1><tt>service_two</center></tt></h1>')
def test_case3(request):
    return HttpResponse('<center><h1><tt>service_three</center></tt></h1>')
def test_case4(request):
    return HttpResponse('<center><h1><tt>service_four</center></tt></h1>')
def test_case5(request):
    return HttpResponse('<center><h1><tt>service_five</center></tt></h1>')

