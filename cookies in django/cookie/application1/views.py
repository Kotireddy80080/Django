from django.shortcuts import render
def test_case1(request):
    response=render(request,"application1/s1.html")
    response.set_cookie("name","i_am_working_as_a_developer")
    return response
def test_case2(request):
    name=request.COOKIES.get("name","cookies are not found....")
    return render(request,"application1/s2.html",{'name':name})
def test_case3(request):
    reponse=render(request,"application1/s3.html")
    reponse.delete_cookie("name")
    return reponse

