from django import forms

class regform(forms.Form):
    usname=forms.CharField(max_length=30)
    name=forms.CharField(max_length=30)
    phone=forms.IntegerField()
    email=forms.EmailField()
    pswd=forms.CharField(max_length=20)
    cpswd=forms.CharField(max_length=20)

class logform(forms.Form):
    email=forms.CharField(max_length=30)
    pswd=forms.CharField(max_length=20)