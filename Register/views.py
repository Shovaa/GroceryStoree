from django.shortcuts import render, redirect
from django.http import HttpResponse
from Register.models import register

# Create your views here.
def Register(request):
    

    if request.method == 'POST':
        Username = request.POST['Username']
        Password= request.POST['Password']
        ContactInfo= request.POST['ContactInfo']
        Fullname = request.POST['FullName']
        ConfrimPassword= request.POST['ConfrimPassword']

        if Password==ConfrimPassword:  
           user = register(Username= Username,Password=Password, ContactInfo=ContactInfo, FullName= Fullname, ConfrimPassword=ConfrimPassword)
           user.save();
           print("user created")
           return redirect('/Home')

        else:
            print("password dosent match")
    

    else:
      return render(request,'register.html')
      
    