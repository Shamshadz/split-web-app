from multiprocessing import context
from django.contrib import messages
from split_app.models import bill,payee
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login,logout as auth_logut
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'split_app/home.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            auth_login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "split_app/home.html",{"fname":fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')


    return render(request, 'split_app/login.html')

def logout(request):
    auth_logut(request)
    return redirect('index')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        
        messages.success(request, "Your Account is has been created")

        return redirect('login')

    return render(request, 'split_app/signup.html')


@login_required
def page(request):

    if request.method == 'POST':
        description = request.POST['description']
        price = request.POST['price']
        name = request.POST.getlist('name')  #getlist
        pay = request.POST.getlist('pay')

        pay1 = bill(description=description,price=price)
        pay1.user = request.user
        pay1.save()

        for name, pay in zip(name, pay):     # zip is something different
            mypayee = payee(billId=pay1,name=name,pay=int(pay))
            mypayee.save()

    return render(request, 'split_app/page.html',)

# def page(request):

#     if request.method == 'POST':
#         description = request.POST['description']
#         price = request.POST['price']
#         name = request.POST.getlist('name')  #getlist
#         mobile = request.POST.getlist('mobile')

#         pay = bill(description=description,price=price)
#         pay.save()

#         for name, mobile in zip(name, mobile):     # zip is something different
#             mypayee = payee(billId=pay,name=name,mobile=int(mobile))
#             mypayee.save()

@login_required
def pay(request):

    # add = bill.objects.all()
    add = bill.objects.filter(user=request.user)
    
    context = {'add': add}

    return render(request, 'split_app/pay.html',context)

# def pay(request):

#     add = bill.objects.all()
    
#     context = {'add': add}

#     return render(request, 'split_app/pay.html',context)

def delete_paid(request, bill_id):
    billpaid = bill.objects.get(pk=bill_id)
    billpaid.delete()
    return redirect('pay')