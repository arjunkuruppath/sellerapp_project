import os
from django.core.checks import messages
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
# from .forms import EditForm
from .models import *
from django.http import HttpResponse
# Create your views here.
from django.conf import settings
# from ..sellingapp_project import settings
from django.contrib.auth.models import auth
from django.contrib.auth import logout, authenticate, login
from datetime import datetime

# from .forms import UserUpdateForm,ProfileUpdateForm,UserForm

def landing(request):
    return render(request, 'landing.html')


def index(request):
    data = Product.objects.all()
    return render(request, "index.html", {'Product': data})


def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        name = request.POST['firstname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['cpassword']
        profile = request.FILES['profile']
        if password == password2:
            # if User.objects.filter(email=email).exists():
            #     messages.info(request, 'username already taken')
            #     return redirect('log')
            # else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=name,
                                            phone=phone, profile=profile)
            user.save()

            # send_mail('Registration successful', 'Login to see more!!', settings.EMAIL_HOST_USER, [email])

            return render(request, 'login.html')

        else:
            messages.info(request, 'password is not matching...')
            return redirect('reg')
    return render(request, 'registration.html')


def eml(request):
    return render(request, 'email send.html')


def log(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email, password)
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('indexpage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('reg')
    return render(request, "login.html")


def show_profile(request):
    data = User.objects.get(username=request.user)
    print(data)
    return render(request, "show_profile.html", {'obj': data})


def edit_profile_confirm(request):
    data = User.objects.get(username=request.user)
    print(data)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(data.profile) > 0:
                os.remove(data.profile.path)
            data.profile = request.FILES['profile']
        data.first_name = request.POST.get('first_name')
        data.username = request.POST.get('username')
        data.phone = request.POST.get('phone')
        data.email = request.POST.get('email')
        data.save()
        messages.success(request, " Updated Successfully")
        return redirect('show_profile')

    context = {'data': data}
    return render(request, 'edit_profile.html', context)


def edit_profile(request):
    data = User.objects.get(username=request.user)
    return render(request, "edit_profile.html", {'obj': data})


def logoutfn(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('landing')


def post_product(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_desc = request.POST.get('product_desc')
        category = request.POST.get('category')
        location = request.POST.get('location')
        product_price = request.POST.get('product_price')
        product_img = request.FILES.get('product_img')
        time = datetime.now()
        formated_time = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            user_id = User.objects.get(username=request.user)
        except User.DoesNotExist:
            user_id = ''

        Product(product_name=product_name, product_desc=product_desc, category=category, location=location,
                product_price=product_price, product_img=product_img, time=formated_time,userid = user_id).save()
        return redirect('indexpage')

    return render(request, 'post_product.html')

def product_detail(request,id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "product_detail.html", context)

def my_post(request):
    userid = request.user
    data = Product.objects.filter(userid_id=request.user)
    print(data)
    return render(request, "my_post.html", {'Product': data , 'userid' : userid})

def edit_post_confirm(request):
    data = Product.objects.get(product_name=request.product_name)
    print(data)
    if request.method == "POST":
        if len(request.FILES) != 0:
            if len(data.product_img) > 0:
                os.remove(data.product_img.path)
            data.product_img = request.FILES['product_img']
        data.product_name = request.POST.get('product_name')
        data.product_desc = request.POST.get('product_desc')
        data.category = request.POST.get('category')
        data.location = request.POST.get('location')
        data.product_price = request.POST.get('product_price')
        data.save()
        messages.success(request, " Updated Successfully")
        return redirect('my_post')

    context = {'data': data}
    return render(request, 'edit_post.html', context)


def edit_post(request,id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "edit_post.html", context)
