from django.shortcuts import render
from django.http import HttpResponse
from application1.models import users
def test_case1(request):
    data=users.objects.create(first_name="nivas",last_name="reddy",username="nivas123",p1="nivas123",p2="nivas123",mobile_number="6541239875",email="nivas123@gmail.com")
    data.save()
    return HttpResponse("<h1><tt>Record is inserted successfully....</tt></h1>")
