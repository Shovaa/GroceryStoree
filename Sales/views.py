from django.shortcuts import render

# Create your views here.
def Sales(request):
    return render (request,'sales.html')

def ContractBuyer(request):
    return render (request,"contract.html")    