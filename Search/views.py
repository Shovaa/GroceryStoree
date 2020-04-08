from django.shortcuts import render
from Register.models import items
# Create your views here.
def Search(request):
            if request.method=='GET':
                 ItemName =request.GET.getlist('Search')
                 Items= items(ItemName=ItemName)
            context ={
                 'Items': Items,
                 'ItemName':ItemName
                  }
                
            return (context) 
        