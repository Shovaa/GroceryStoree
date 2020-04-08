from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, redirect
from django.http import HttpResponse



# Create your views here.
def Home(request):
    if request.method == 'GET':
      print("Hello World")
      return render(request, 'home.html')

    else:
         return redirect('/Items') 
        
    