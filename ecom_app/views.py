from django.shortcuts import render, redirect
from django.views import View
from ecom_app.models import Product, Cart, Wishlist
from django.contrib.auth.decorators import  login_required
from ecom_app.models import Payment, OrderPlaced
from user_accounts.models import Profile
from django.http import HttpResponseBadRequest, JsonResponse
from django.db.models import Q
from django.conf import settings
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required    
def home(request):
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            print("yes profile")
            return render(request, "ecom_app/home.html", context={'profile': profile, 'total_item': total_item})
    except:
        print("Profile doesn't exist!!")
    print("no profile")
    return render(request, "ecom_app/home.html",{'total_item': total_item})
    
    
@login_required    
def contact(request):
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/contact.html", context={'profile': profile,'total_item': total_item})
    except:
        print("Profile doesn't exist!!")
    return render(request, "ecom_app/contact.html", {'total_item': total_item})

@login_required    
def about(request):
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/about.html",context={'profile': profile,'total_item': total_item})
    except:
        print("Profile doesn't exist!!")
        
    return render(request, "ecom_app/about.html",{'total_item': total_item})
  
@login_required      
def category(request, category_name):
    total_item = len(Cart.objects.filter(user=request.user))
    all_products = Product.objects.filter(category=category_name)    
    product_names = Product.objects.filter(category=category_name).values('product_name')
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/category.html", context={'products':product_names, 'all_products':all_products, 'profile':profile,'total_item': total_item})
    except:
        print("Profile doesn't exist!!")
    return render(request, "ecom_app/category.html", context={'products':product_names, 'all_products':all_products,'total_item': total_item})
 
 
@login_required     
def specific_product(request, product_name):
    total_item = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(product_name=product_name)    
    product_names = Product.objects.filter(category=product[0].category).values('product_name')
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/category.html", context={'products':product_names, 'all_products':product, 'profile':profile,'total_item': total_item})
            
    except:
        print("Profile doesn't exist!!")
    return render(request, "ecom_app/category.html", context={'products':product_names, 'all_products':product,'total_item': total_item})
    

@login_required    
def product(request, uid):
    total_item = len(Cart.objects.filter(user=request.user))
    product = Product.objects.filter(uid=uid)[0]
    wishlist = Wishlist.objects.filter(Q(user = request.user) & Q(product=product))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/product_page.html", context={'product':product, 'profile':profile,'total_item': total_item, 'wishlist': wishlist})
    except:
        print("Profile doesn't exist!!")
    return render(request, "ecom_app/product_page.html", context={'product':product,'total_item': total_item,'wishlist': wishlist})



def add_to_cart(request, uid):
    product = Product.objects.filter(uid = uid)[0]
    my_user = request.user
    cart = Cart.objects.create(user=my_user, product=product)
    cart.save()
    
    return redirect("/show_cart")    
           
    
    
def show_cart(request):
    my_user = request.user
    cart = Cart.objects.filter(user = my_user)
    total_item = len(Cart.objects.filter(user=request.user))
    
    amount = 0
    for item in cart: 
        if item.product.discounted_price == 0:
            value = item.product.selling_price
        else:
            value = item.product.discounted_price
        price = item.no_of_items * value
        amount += price
    total_amount = amount + 40
    
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/addtocart.html", context={'cart':cart, 'amount':amount, 'total_amount':total_amount, 'profile':profile,'total_item': total_item})
    except:
        return render(request, "ecom_app/addtocart.html", context={'cart':cart, 'amount':amount, 'total_amount':total_amount,'total_item': total_item})


def pluscart(request):
    if request.method == "GET":
        prod_id = request.GET['uid']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        
        c.no_of_items += 1
        c.save()
        
        my_user = request.user
        cart = Cart.objects.filter(user = my_user)
        
        amount = 0
        for item in cart: 
            if item.product.discounted_price == 0:
                value = item.product.selling_price
            else:
                value = item.product.discounted_price
            price = item.no_of_items * value
            amount += price
        total_amount = amount + 40
        
        data = {
            'no_of_items':c.no_of_items,
            'amount': amount,
            'total_amount':total_amount
        }        
        return JsonResponse(data)

    
def minuscart(request):
    if request.method == "GET":
        prod_id = request.GET['uid']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        
        c.no_of_items -= 1
        if c.no_of_items < 1:
            c.no_of_items = 1
        
        c.save()
        my_user = request.user
        cart = Cart.objects.filter(user = my_user)
        
        amount = 0
        for item in cart: 
            if item.product.discounted_price == 0:
                value = item.product.selling_price
            else:
                value = item.product.discounted_price
            price = item.no_of_items * value
            amount += price
        total_amount = amount + 40
        
        data = {
            'no_of_items':c.no_of_items,
            'amount': amount,
            'total_amount':total_amount
        }
        
        print(prod_id)
        return JsonResponse(data)
        
    
def removecart(request):
    if request.method == "GET":
        prod_id = request.GET['uid']
        c = Cart.objects.get(Q(product=prod_id) & Q(user = request.user))
        
        c.delete()
        # c.save()    
        my_user = request.user
        cart = Cart.objects.filter(user = my_user)
        
        amount = 0
        for item in cart: 
            if item.product.discounted_price == 0:
                value = item.product.selling_price
            else:
                value = item.product.discounted_price
            price = item.no_of_items * value
            amount += price
        total_amount = amount + 40
        
        data = {
            'amount': amount,
            'total_amount':total_amount
        }
        
        return JsonResponse(data)
       
@csrf_exempt
def checkout(request): 
    if request.method == "POST":
        amount =  float(request.POST.get('amount')) * 100 # Amount in paise


        # Create a client object for razorpay
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment_data = {
            "amount": amount,
            "currency": "INR",
            "receipt": "order_receipt_17",
            "notes": {
                "email": "sarojv434@gmail.com",
            },
        }

        # Create a razorpay order with above dict data
        order = client.order.create(data=payment_data)
        
        order_id = order['id']
        order_status = order['status']
        if order_status == 'created':
            payment = Payment(
                user = request.user,
                amount = amount,
                razorpay_order_id = order_id,
                razorpay_payment_status = order_status
            )   
            payment.save()
        
        # Include key, name, description in the JSON response
        response_data = {
            "id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "key": settings.RAZOR_KEY_ID,
            "name": "Neel Product",
            "description": "My Payements",
        }
        
        # Sending the json data back to the ajax call
        return JsonResponse(response_data)
    
    my_user = request.user
    cart_items = Cart.objects.filter(user=my_user)
    add = Profile.objects.filter(user=my_user)[0]
    total_item = len(cart_items)
    
    amount = 0
    for item in cart_items: 
        if item.product.discounted_price == 0:
            value = item.product.selling_price
        else:
            value = item.product.discounted_price
        price = item.no_of_items * value
        amount += price
    total_amount = amount + 40
    context = {
        'cart_items': cart_items,
        'add': add,
        'total_amount': total_amount,
        'total_item': total_item
    }
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, 'ecom_app/checkout.html', context={
        'cart_items': cart_items,
        'add': add,
        'total_amount': total_amount,
        'profile': profile,
        'total_item': total_item
    })
    except:
        return render(request, 'ecom_app/checkout.html', context=context)
        
    
    


def payment_success(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    profile_uid = request.GET.get('profile_uid')
    my_user = request.user
    
    print(profile_uid)
    
    # accessing the profile
    profile = Profile.objects.get(uid=profile_uid)
    
    print(profile)  
    # accessing the payment model
    payment = Payment.objects.get(razorpay_order_id = order_id)
    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.save()
    
    # updating the cart after payment
    cart_items = Cart.objects.filter(user = my_user)
    
    for cart in cart_items:
        OrderPlaced(user=my_user, profile=profile, product = cart.product, no_of_items = cart.no_of_items).save()
        cart.delete()
    return redirect("orders")


def payment_failed(request):
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/payment_failed.html", context={'profile': profile, 'total_item': total_item})
    except:
        return render(request, "ecom_app/payment_failed.html",{ 'total_item': total_item})
    
    
def orders(request):
    orders = OrderPlaced.objects.filter(user=request.user)
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/orders.html", context={"orders": orders,'profile': profile, 'total_item': total_item})
    except:  
        return render(request, "ecom_app/orders.html", context={"orders": orders,'total_item': total_item})
 


def plus_wishlist(request):
    prod_uid = request.GET["prod_uid"]
    product = Product.objects.get(uid=prod_uid)
    my_user = request.user
    wishlist = Wishlist.objects.create(user=my_user, product=product)
    wishlist.save()
    
    data = {
        'message':'Added to wishlist successfully!!'
    }
    return JsonResponse(data)



def minus_wishlist(request):
    prod_uid = request.GET["prod_uid"]
    my_user = request.user
    product = Product.objects.get(uid=prod_uid)
    wishlist = Wishlist.objects.filter(Q(product=product) & Q(user=my_user))
    wishlist.delete()
    
    data = {
        'message':'Removed from wishlist successfully!!'
    }
    
    return JsonResponse(data)


def show_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    total_item = len(Cart.objects.filter(user=request.user))
    print(wishlist)
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, 'ecom_app/wishlist.html', {'profile': profile, 'total_item': total_item, 'wishlist': wishlist})
    except:
        return render(request, 'ecom_app/wishlist.html', {'total_item': total_item, 'wishlist': wishlist})
        
    
    


def search(request):
    query = request.GET["search"]
    product = Product.objects.filter(product_name__icontains = query)
    print(product)
    total_item = len(Cart.objects.filter(user=request.user))
    try:
        profile = Profile.objects.all()[0]
        if profile is not None:
            return render(request, "ecom_app/search.html", context={'product': product, 'total_item':total_item, 'profile': profile})
    except:
        return render(request, "ecom_app/search.html", context={'product': product, 'total_item':total_item})
        