from django.shortcuts import render, redirect
from django.http import HttpResponse
from Register.models import items
# Create your views here.


# Create your views here.
def Items(request):
    

    if request.method == 'POST':
        ItemName = request.POST['ItemName']
        Quantity= request.POST['Quantity']
        Price= request.POST['Price']
        Date = request.POST['Date']
        Total=request.POST['Total']
        


        product = items(ItemName=ItemName,Quantity=Quantity, Price=Price, Date=Date, Total=Total)
        product.save();
        print("Items Added")
        return redirect('/Items')
    

    else:
      return render(request, 'items.html')
      