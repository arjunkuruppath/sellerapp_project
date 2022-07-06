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

urlpatterns = [
    path('',landing,name='landing'),
    path('index/',index,name='indexpage'),
    path('reg/',reg,name='reg'),
    path('success/',eml,name='eml'),
    path('log/',log,name='log'),
    path('show_profile/', show_profile, name='show_profile'),
    path('edit_profile_confirm/', edit_profile_confirm, name='edit_profile_confirm'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('logout/',logoutfn,name='logout'),
    path('post_product/', post_product, name='post_product'),
    path('product_detail/<id>/', product_detail, name='product_detail'),
    path('my_post/', my_post, name='my_post'),
    path('edit_post_confirm/<id>/', edit_post_confirm, name='edit_post_confirm'),
    path('edit_post/<id>', edit_post, name='edit_post'),
    path('sendmail/<id>', sendmail, name='sendmail'),

    path('applied_product/', applied_product, name='applied_product'),

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
