"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',LandingPage.as_view(),name='landing'),
    path('index/',IndexView.as_view(),name='indexpage'),
    path('reg/',RegistrationView.as_view(),name='reg'),
    path('success/',eml,name='eml'),
    path('log/',LoginView.as_view(),name='log'),
    path('show_profile/', ShowProfile.as_view(), name='show_profile'),
    path('edit_profile_confirm/', EditProfileConfirm.as_view(), name='edit_profile_confirm'),
    path('edit_profile/', EditProfile.as_view(), name='edit_profile'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path('post_product/', PostProductView.as_view(), name='post_product'),
    path('product_detail/<id>/', ProductDetail.as_view(), name='product_detail'),
    path('my_post/', MyPost.as_view(), name='my_post'),
    path('edit_post_confirm/<id>/', EditPostConfirm.as_view(), name='edit_post_confirm'),
    path('edit_post/<id>', EditPost.as_view(), name='edit_post'),
    path('deletedata/<str:pk>', DeleteProductView.as_view(), name='deletedata'),
    path('sendmail/<id>', SendMail.as_view(), name='sendmail'),
    path('applied_product/', AppliedProduct.as_view(), name='applied_product'),
    path('buyer_list/<id>/', BuyersList.as_view(), name='buyer_list'),
    path('accept_interest/<id>/<pk>/', AcceptInterest.as_view(), name='accept_interest'),
    path('reject_interest/<id>/<pk>/', RejectInterest.as_view(), name='reject_interest'),
    path('search/',SearchResult.as_view(), name='search'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_complete"),
]
