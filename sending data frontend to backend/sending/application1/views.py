from django.shortcuts import render 
from application1.models import employees
from application1.forms import employees_Forms 
def Test_Case1(request):
    form=employees_Forms()
    if request.method=="POST":
        form=employees_Forms(request.POST)
        if(form.is_valid()):
            form.save() 
    context={'form':form}
    return render(request,"application1/S1.html",context)