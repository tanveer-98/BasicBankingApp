from django.urls import path,include
from django.conf.urls import url
from app1 import views
urlpatterns=[
    path('',views.home,name='home'),
    path('customers/',views.customers,name='customers'),
    path('cdetails/<str:pk>',views.cdetails,name='cdetails'),
]
