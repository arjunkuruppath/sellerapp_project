import os
from django.conf.global_settings import EMAIL_HOST_USER
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
from django.contrib.auth.decorators import login_required


# from .forms import UserUpdateForm,ProfileUpdateForm,UserForm

def landing(request):
    data = Product.objects.all()
    return render(request, 'index.html', {'data': data})


def index(request):
    product_data = Product.objects.all()
    user_data = User.objects.get(username=request.user)
    context = {}
    context['data'] = product_data
    context['user_data'] = user_data
    print(user_data.is_active)
    return render(request, "index.html", context)


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
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('reg')
            elif User.objects.filter(phone=phone).exists():
                messages.info(request, 'phone number already taken')
                return redirect('reg')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('reg')
            else:
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
        # print(email, password)
        user = authenticate(username=email, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            return redirect('indexpage')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('reg')
    return render(request, "login.html")


@login_required(login_url='/log/')
def show_profile(request):
    data = User.objects.get(username=request.user)
    # print(data)
    return render(request, "show_profile.html", {'obj': data})


@login_required(login_url='/log/')
def edit_profile_confirm(request):
    data = User.objects.get(username=request.user)
    # print(data)
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


@login_required(login_url='/log/')
def edit_profile(request):
    data = User.objects.get(username=request.user)
    return render(request, "edit_profile.html", {'obj': data})


def logoutfn(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('landing')


@login_required(login_url='/log/')
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
                product_price=product_price, product_img=product_img, time=formated_time, userid=user_id).save()

        SellerData(product_name=product_name,email=request.user.email,seller_name=request.user,seller_price=product_price).save()
        return redirect('indexpage')

    return render(request, 'post_product.html')


@login_required(login_url='/log/')
def product_detail(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "product_detail.html", context)


@login_required(login_url='/log/')
def my_post(request):
    userid = request.user
    data = Product.objects.filter(userid_id=request.user)
    # print(data)
    return render(request, "my_post.html", {'Product': data, 'userid': userid})


def edit_post_confirm(request, id):
    data = Product.objects.get(id=id)
    # print(data)
    return render(request, 'edit_post.html', {'data': data})


@login_required(login_url='/log/')
def edit_post(request, id):
    data = Product.objects.get(id=id)
    # print(data.id)
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
    else:
        return render(request, 'edit_post.html')


def deletedata(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('my_post')


def sendmail(request, id):
    if request.method == 'POST':
        seller_name = Product.objects.get(id=id)
        buyer_name = request.user
        product_id = id
        buyer_price = request.POST['show_interest']
        buyer_status = False
        BuyProduct(seller_name=seller_name.userid, buyer_name=buyer_name, product_id=product_id, buyer_price=buyer_price,
                   buy_status=buyer_status).save()
        recepient_mailid = seller_name.userid.email
        subject = "This is Product interest message"
        message = f'This is a verification msg ,interested product { seller_name.product_name } interested price { buyer_price}'
        recepient =recepient_mailid
        send_mail( subject,message,settings.EMAIL_HOST_USER, [recepient], fail_silently=False)
        messages.success(request, "sucessfuly sent a approved mail")
    #
    return redirect('indexpage')


def applied_product(request):
    userid = request.user
    data = BuyProduct.objects.filter(buyer_name=request.user).values('product_id')
    li = []
    try:
        for product_id in data:
            print(product_id['product_id'])
            product_details = Product.objects.get(id=product_id['product_id'])
            li.append(product_details)
            return render(request, "applied_product.html", {'BuyProduct': li})
    except Product.DoesNotExist:
        return HttpResponse("You haven't applied any products yet!!")
    return HttpResponse("You haven't applied any products yet")


def buyer_list(request,id):
    data = BuyProduct.objects.filter(product_id=id)
    product_name = Product.objects.get(id=id)
    print(product_name)
    return render(request,'buyer_list.html',{'obj' : data , 'product_name' : product_name })


def accept_interest(request,id,pk):
    buy_product = BuyProduct.objects.get(id=id)
    print(pk,id)
    seller_name = buy_product.seller_name
    product_name = Product.objects.get(id=pk)
    buyer_price = buy_product.buyer_price
    buyer_name = buy_product.buyer_name
    buyer_email = Product.objects.get(id=pk).userid.email
    print(seller_name,buyer_price,buyer_name)
    subject = f"Hi {buyer_name}"
    message = f'{seller_name} has accepted your request to buy {product_name} for {buyer_price}'
    recepient = buyer_email
    send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)
    return redirect('indexpage')