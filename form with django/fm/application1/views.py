from django.shortcuts import render
from application1.forms import employee_Regestration
def test_case1(request):
    data=employee_Regestration()
    return render(request,"application1/s1.html",{'data':data})
