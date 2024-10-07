from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from restaurant.models import *
from customer.models import *
from users.models import User
from django.http import HttpResponseRedirect
from django.db.models import Sum
from django.http import JsonResponse

@login_required(login_url='/login/')
def index(request):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()
    sliders = Slider.objects.all()
    context = {
        "store_categories": store_categories,
        "stores": stores,
        "sliders": sliders
    }
    return render(request, 'web/index.html', context=context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login  (request,user)
            return HttpResponseRedirect(reverse('web:index'))
        
        else:
            context = {
                'error': True,
                'message': 'Invalid  Email or Password'
            }
            return render(request, 'web/login.html', context=context)
            
        
    else:
        return render(request, 'web/login.html')
    
def  validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_valid' : User.objects.filter(email__iexact=email).exists()
    }
    return JsonResponse(data)

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if User.objects.filter(email=email).exists():
            context = {
                'error': True,
                'message': 'Email Aleardy Exists'
            }
            return render(request, 'web/register.html', context=context)
        
        else:
            
        
        
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
                is_customer=True
            )
            user.save()
            customer = Customer.objects.create(
                user=user
            )
            customer.save()
            return HttpResponseRedirect(reverse('web:login'))
    else:
        return render(request, 'web/register.html')
    
    
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:login'))


@login_required(login_url='/login/')
def restaurants(request,id):
    store_categories = StoreCategory.objects.all()
    stores = Store.objects.all()
    
    selected_category = StoreCategory.objects.get(id=id)
    
    stores = stores.filter(category=selected_category)
    
    context = {
        "store_categories": store_categories,
        "stores": stores
        
        
    }
    return render(request, 'web/restaurants.html', context=context)


@login_required(login_url='/login/')
def single_rest(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    store = Store.objects.get(id=id)
    foods = Food.objects.filter(store=store)
    foodcategories = FoodCategory.objects.filter(store=store)
    carts = Cart.objects.filter(store=store,customer=customer)
    
    cart_quantities = {cart.product: cart.quantity for cart in carts}
    prod_with_qty =[(food, cart_quantities.get(food, 0)) for food in foods]



            
    context = {
        "store": store,
        "foods": foods,
        "foodcategories": foodcategories,
        "customer": customer,
        "carts": carts,
        "prod_with_qty":prod_with_qty,


        }
    return render(request, 'web/single_rest.html', context=context)    




@login_required(login_url='/login/')
def cart(request):
    customer = Customer.objects.get(user=request.user)
    cart_items = Cart.objects.filter(customer=customer)

    if cart_items.exists():
        cart_amount = cart_items.aggregate(Sum('price'))['price__sum']
        store = cart_items.first().store
    else:
        store = None
        cart_amount = 0

    delivery_charge = 50

    # Handle CartBill
    if CartBill.objects.filter(customer=customer).exists():
        cartbill = CartBill.objects.get(customer=customer)
        cartbill.item_total = cart_amount
        cartbill.totel_amount = cart_amount + delivery_charge - float(cartbill.offer_amount)
        cartbill.save()
    else:
        cartbill = CartBill.objects.create(
            customer=customer,
            item_total=cart_amount,
            delivery_charge=delivery_charge,
            totel_amount=cart_amount + delivery_charge,
            offer_amount=0
        )

    error_message = None

    if request.method == 'POST':
        code = request.POST.get('code')
        try:
            offer = Offer.objects.get(code=code)
            if offer.is_percentage:
                discount = round((offer.discount / 100) * cart_amount)
            else:
                discount = offer.discount

            cartbill.offer_amount = discount
            cartbill.total_amount = cart_amount + delivery_charge - float(discount)
            cartbill.save()
            success_message = 'Coupon code applied successfully!'
        except Offer.DoesNotExist:
            error_message = 'Invalid coupon code. Please try again.'

    address = cartbill.address


    context = {
        "customer": customer,
        "cart_items": cart_items,
        "cart_amount": cart_amount,
        "store": store,
        "cartbill": cartbill,
        "address": address,
        "error_message": error_message,
        "success_message": success_message if 'success_message' in locals() else None,
    }

    return render(request, 'web/cart.html', context=context)



    
@login_required(login_url='/login')
def add_cart(request, id):
    customer = Customer.objects.get(user=request.user)
    product = Food.objects.get(id=id)
    cart= Cart.objects.create(
        product=product, 
        customer=customer,
        quantity=1,
        price=product.price,
        store=product.store,        
    )
    cart.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='/login/')
def cart_plus(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    product = Food.objects.get(id=id)
    cart = Cart.objects.get(customer=customer,product=product)
    cart.quantity += 1
    cart.price += product.price
    cart.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/login/')
def cart_minus(request,id):
    user = request.user
    customer = Customer.objects.get(user=user)
    product = Food.objects.get(id=id)
    cart = Cart.objects.get(customer=customer,product=product)
    
    cart.quantity -= 1
    cart.price -= product.price
    if cart.quantity == 0:
        cart.delete()
    else: 
        cart.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    



@login_required(login_url='/login/')
def add_address(request):            
    user = request.user
    customer = Customer.objects.get(user=user)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')
        phone_number = request.POST.get('phone_number')
        

        address = Address.objects.create(
            customer=customer,
            address=address,
            appartment=appartment,
            landmark=landmark,
            phone_number=phone_number,
            address_type=address_type,
        )
        address.save()
        return HttpResponseRedirect(reverse('web:address'))
    else:    
        return render(request, 'web/add_address.html',)
    
@login_required(login_url='/login')
def address(request):
    customer = Customer.objects.get(user=request.user)
    current_address = Address.objects.filter(customer=customer)
    context = {
        'customer': customer,
        'current_address': current_address,
    }

    return render(request, 'web/address.html', context=context)
@login_required(login_url='/login/')
def address_delete(request,id): 
    address = Address.objects.get(id=id)
    address.delete() 
    
    return HttpResponseRedirect(reverse('web:address'))
    

@login_required(login_url='/login/')
def address_edit(request,id):            
    user =request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.get(id=id, customer=customer)

    if request.method == 'POST':
        address = request.POST.get('address')
        appartment = request.POST.get('appartment')
        landmark = request.POST.get('landmark')
        address_type = request.POST.get('address_type')
        phone_number = request.POST.get('phone_number')
        
        address = Address.objects.create(
            customer=customer,
            address=address,
            appartment=appartment,
            landmark=landmark,
            phone_number=phone_number,
            address_type=address_type,
        )
        address.save()
        return HttpResponseRedirect(reverse('web:address'))
        
    else:
        return render(request, 'web/add_address.html', {'address': address, 'is_edit': True})
    
    

@login_required(login_url='/login/')
def address_select(request,id): 
    user = request.user
    customer = Customer.objects.get(user=user)
    address = Address.objects.get(id=id)
    cartbill = CartBill.objects.get(customer=customer)
    cartbill.address = address
    cartbill.save() 
    
    return HttpResponseRedirect (reverse('web:cart'))



@login_required(login_url='/login/')
def creat_order(request): 
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = Cart.objects.filter(customer=customer) 
    cartbill = CartBill.objects.get(customer=customer)
    
    order = Order.objects.create(
          customer=customer,
          item_total= cartbill.item_total,
          delivery_charge= cartbill.delivery_charge,
          totel_amount= cartbill.totel_amount,
          offer_amount= cartbill.offer_amount,
          address = cartbill.address
    )
    
    order.save()
    
    
    for cart in cart_items:
        order_bill = OrderBill.objects.create(
        customer=customer,
        product = cart.product,
        store = cart.store,
        quantity = cart.quantity,
        price = cart.price,        
        )
        
        order.cartbill.add(order_bill)
        order_bill.save()
        order.save()
        cart.delete()
        
    previous_order = Order.objects.all().order_by('-id').first()
    
    
    if previous_order is not None:
        last_id = previous_order.id
        order_id = f'ORD{last_id + 1:03d}'
    else:
        order_id = "ORD001"

    order.order_id = order_id
    order.save()
 
        
    return HttpResponseRedirect (reverse('web:order'))

    
@login_required(login_url='/login/')
def checkout(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    
    try:
        cartbill = CartBill.objects.get(customer=customer)
    except CartBill.DoesNotExist:
        cartbill = None
        
    context = {
        'item_total': cartbill.item_total or 0,
        'offer_amount': cartbill.offer_amount or 0,
        'delivery_charge': cartbill.delivery_charge if cartbill else 0,
        'totel_amount': cartbill.totel_amount if cartbill else 0,
    }
        
    return render(request, 'web/checkout.html', context=context)  

@login_required(login_url='/login/')
def offer(request):            
    
    return render(request, 'web/offer.html') 
@login_required(login_url='/login/')
def single_order(request,id):  
    user = request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.get(id=id) 
    
    
    context = {
        'order': order,  
        }
    return render(request, 'web/single_order.html', context=context) 
    

@login_required(login_url='/login/')
def order(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    orders = Order.objects.filter(customer=customer).prefetch_related('cartbill')    
    
    
    context = {
        'orders': orders,  
        }
    return render(request, 'web/order.html', context=context) 
def account(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    order = Order.objects.filter(customer=customer).prefetch_related('cartbill')[:3]
    
    
    context = {
        'order': order,  
        }
    return render(request, 'web/account.html', context=context) 