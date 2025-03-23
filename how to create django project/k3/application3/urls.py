from django.conf.urls import url
from application3 import views

urlpatterns = [
    url(r'^t1/', views.test_case1),
    url(r'^t2/', views.test_case2),
    url(r'^t3/', views.test_case3),
    url(r'^t4/', views.test_case4),
    url(r'^t5/', views.test_case5),
]
