from django.shortcuts import render
def test_case1(request):
    request.session['name']='i_hub_services'
    return render(request,"application1/s1.html")
def test_case2(request):
    name=request.session.get('name',default="session out")
    return render(request,"application1/s2.html",{"name":name})
def test_case3(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,"application1/s3.html")