from datetime import datetime, timedelta

from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from taskapp.models import branch, place, userdetail, item


def home(request):
    br = branch.objects.all()
    return render(request,"home.html",{'branch':br})
def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('taskapp:allcat')
        else:
            messages.info(request, "Invalid credentials")
            return redirect('taskapp:log')
    return render(request, "login.html")


def regis(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exists")
                return redirect('taskapp:regis')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('taskapp:regis')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                messages.info(request,"Registation successfull")
                return redirect('taskapp:log')

        else:
            messages.info(request, "Password and confirm password should be same.")
            return redirect('taskapp:regis')
    return render(request,"index.html")


def lout(request):
    auth.logout(request)
    return redirect('taskapp:home')

def allcat(request):
    return render(request,"ask.html")



def detail(request):
    br = branch.objects.all()
    pro=item.objects.all()
    current_time = datetime.now()
    n = 1
    future_time = current_time + timedelta(hours=n)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        ph = request.POST['ph']
        add = request.POST['add']
        place = request.POST['place']
        productid = request.POST['prod']
        quantity = request.POST['quantity']
        print(quantity)
        productstock  = item.objects.get(id=productid)
        print(productstock)
        if productstock.stock < int(quantity):
            messages.info(request, "Sorry! We don't have enough stock for your order.")
            return redirect('/detail')
        else:
            res = userdetail.objects.create(name=name, email=email, ph=ph, add=add, place=place,
                                            quantity=quantity, delivery=future_time,prod=productid)

            res.save()
            productstock.stock -= int(quantity)
            productstock.save()
            return redirect('taskapp:info')
    return render(request, "index3.html",{'dist': br,'pro':pro})

def load_branches(request):
    place_id=request.GET.get('dist')
    pla=place.objects.filter(branch_id=place_id).all()
    return render(request, "dropdown_list.html",{'place':pla})


# def neww(request):
#     current_time = datetime.now()
#     n = 40
#     future_time = current_time + timedelta(minutes=n)
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         ph = request.POST['ph']
#         add = request.POST['add']
#         dis = request.POST['dist']
#         place = request.POST['place']
#         quantity = request.POST['quantity']
#         p = request.POST['prod']
#         pr = ''.join([i for i in p if not i.isdigit()])
#         pro = item.objects.get(product=pr)
#         if quantity > item.pro.stock:
#             messages.info(request, "Please choose less quantity")
#             return redirect('taskapp:detail')
#         else:
#             res = userdetail.objects.create(name=name, email=email, ph=ph, add=add, prod=pr, place=place,
#                                             quantity=quantity, delivery=future_time)
#             res.save()
#     return render(request,"index3.html")
def info(request):
    current_time = datetime.now()
    n = 40
    future_time = current_time + timedelta(minutes=n)
    return render(request,"info.html",{'time':future_time})