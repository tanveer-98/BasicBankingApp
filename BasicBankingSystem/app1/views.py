from django.shortcuts import render,redirect
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
    person1 = customer.objects.get(id= pk)
    # person1 is the Sender
    # person2 is the receiver
    person2 = customer.objects.get(id= pk1)

    if request.method== 'POST':
        data = request.POST
        bal1 = person1.current_balance
        bal2 = person2.current_balance
        if  bal1>int(data['amount']):

            person2.current_balance = person2.current_balance + int(data['amount'])
            person1.current_balance = person1.current_balance - int (data['amount'])
            person2.save()
            person1.save()
        else:
            return redirect('invalid')


    return render(request,'Transfer/transfer.html',{'person1':person1,'person2':person2})

def invalid(request):
    return render(request,'InvalidTransaction/invalid.html')
