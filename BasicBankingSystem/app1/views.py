from django.shortcuts import render,redirect
from app1.models import customer
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'homepage/home.html')


def customers(request):

    cust = customer.objects.all()
    return render(request,'customers/CustomerPage.html',{'cust':cust})


def check(name):
    persons = customer.objects.all()
    for x in persons:
        if name.lower() == x.name.lower():
            return {'p':x,'r':True}
    return {'p':None,'r':False}

def cdetails(request,pk):
    allCust = customer.objects.all()

    CurrCust = customer.objects.get(id=pk)

    if request.method== 'POST':
        person1 = customer.objects.get(id= pk)
        # person1 is the Sender
        # person2 is the receiver

        data = request.POST
        result = check(data['cname'])
        if result['r']:
            person2 = result['p']

            bal1 = person1.current_balance
            bal2 = person2.current_balance
            if  data['amount'] != None and bal1>int(data['amount']) :

                person2.current_balance = person2.current_balance + int(data['amount'])
                person1.current_balance = person1.current_balance - int (data['amount'])
                person2.save()
                person1.save()
                messages.success(request,'The Transaction Was Successful')
            else:
                if bal1<int(data['amount']):
                    messages.error(request,'Insufficient Balance')
                else:
                    messages.error(request,'Invalid Amount Input')
        else:
            messages.error(request,'Person does not exist in Database')

    return render(request,'customerDetails/details.html',{'CurrCust':CurrCust,'allCust':allCust})
