from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Items,ItemDetails,Cart
from django.contrib.auth.decorators import login_required
# Create your views here.


def showlaptop(request):
    template = loader.get_template('showlaptop.html')
    laptop=ItemDetails.objects.select_related('itemsid')

    print(laptop.query)
    return HttpResponse(template.render({'laptop':laptop,'request':request}))


def lapdetails(request,id):
     template = loader.get_template('laptopdetails.html')
     currentuser=request.user
     print(currentuser.id)
     laptop=ItemDetails.objects.select_related('itemsid').filter(id=id)
     context={
         'laptop':laptop,
         'request':request
         }
     return HttpResponse (template.render(context))


@login_required(login_url='/auth_login/')
def checkout2(request,id):
       template=loader.get_template('checkout.html')
       current_user = request.user.id
       cart=Cart.objects.all().filter(Id_user=current_user,Id_product=id).first()
       product=Items.objects.get(id=cart.Id_product)
       context={
            'cart':cart,
            'productname':product,
             'request':request
            
       }
       return HttpResponse(template.render(context=context)) 

def add_to_cart2(request,id): 
    currentuser=request.user 
    discount=2 
    status=False 
    phone=ItemDetails.objects.select_related('itemsid').filter(id=id) 
    count=0 
    for item in phone: 
        net=item.total-discount 
        count=count+1 
    cart = Cart( 
     Id_product=item.id, 
     Id_user=currentuser.id, 
     price=item.price, 
     qty=item.qty, 
     tax=item.tax, 
     total=item.total, 
     discount=discount, 
     net=net, 
     status=status 
) 
    currentuser=request.user.id 
    count=Cart.objects.filter(Id_user=currentuser).count() 
    print(count) 
    cart.save() 
    request.session['countcart']=count 
    return redirect("/showlaptop")