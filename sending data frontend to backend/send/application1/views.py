from django.shortcuts import render
from application1.models import student
from application1.forms import student_Forms
def test_case1(request):
    form=student_Forms()
    if request.method=="POST":
        form=student_Forms(request.POST)
        if(form.is_valid()):
            form.save()
    context={'form':form}
    return render(request,"application1/s1.html",context)