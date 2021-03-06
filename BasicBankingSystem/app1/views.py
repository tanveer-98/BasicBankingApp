from django.shortcuts import render
from app1.models import customer
# Create your views here.
def home(request):
    return render(request,'homepage/home.html')


def customers(request):

    cust = customer.objects.all()
    return render(request,'customers/CustomerPage.html',{'cust':cust})

def cdetails(request,pk):
    allCust = customer.objects.all()
    CurrCust = customer.objects.get(id=pk)
    return render(request,'customerDetails/details.html',{'CurrCust':CurrCust,'allCust':allCust})


def transfer(request,pk,pk1):
    return render(request,'Transfer/transfer.html')
