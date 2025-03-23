from django.shortcuts import render
from application1.models import products1
from django.http import HttpResponse
def test_case1(request):
    try:
        obj1=products1.objects.get(pid=1001)
    except:
        return HttpResponse("<h1><tt>dear user data not found</tt><h1>")
    return HttpResponse(obj1)
