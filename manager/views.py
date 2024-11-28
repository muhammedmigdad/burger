from django.shortcuts import render, reverse, redirect
from restaurant.models import *
from customer.models import *
from django.http import HttpResponseRedirect, HttpResponse
from manager.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from main.functions import generate_form_errors
from main.decorators import allow_manager

@allow_manager
@login_required(login_url='/login/')
def index(request):
    
    return render(request,'manager/index.html')

def login(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_manager: 
                    auth_login  (request,user)
                    return redirect('manager:index') 
                else:
                    messages.error(request, "Unauthorized access.")
                    return HttpResponse("unauthorized", status=401)
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Form is invalid.")
    else:
        form = ManagerLoginForm()

    return render(request, 'manager/login.html', {'form': form})

def logout(request):
    return redirect('manager:login')
@allow_manager
@login_required(login_url='/login/')
def store_categories(request):
    instances = StoreCategory.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/store_categories.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def store_category_delete(request,id):
    instance = StoreCategory.objects.get(id=id)
     
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:store_categories'))
@login_required(login_url='/login/')
def store_category_add(request,):
    if request.method == 'POST':   
        form = StoreCategoryform(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:store_categories'))
            
        else:
            message = generate_form_errors(form)
            form = StoreCategoryform()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/store_categories_add.html', context=context)



    else:
        form = StoreCategoryform()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/store_categories_add.html', context=context)
@login_required(login_url='/login/')
def store_category_edit(request, id):
    instance = StoreCategory.objects.get(id=id)
    if request.method == 'POST':   
        form = StoreCategoryform(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:store_categories'))
            
        else:
            message = generate_form_errors(form)
            form = StoreCategoryform()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance,
            }
    
        return render(request,'manager/store_categories_add.html', context=context)



    else:
        form = StoreCategoryform(instance=instance)
        
        context = {
            "form": form,
            "instance": instance,
        }
        
    return render(request,'manager/store_categories_add.html', context=context)
        
    
@allow_manager
@login_required(login_url='/login/')

def store(request):
    instances = Store.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/store.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def store_delete(request,id):
    instance = Store.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:store'))
@allow_manager
@login_required(login_url='/login/')
def store_add(request,):
    if request.method == 'POST':   
        form = Storeform(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:store'))
            
        else:
            message = generate_form_errors(form)
            form = Storeform()

            context = {
            "error": True,
            "message": message,
            "form": form,  
            }
    
        return render(request,'manager/store_add.html', context=context)



    else:
        form = Storeform()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/store_add.html', context=context)

@allow_manager
@login_required(login_url='/login/')
def store_edit(request, id):
    instance = Store.objects.get(id=id)
    if request.method == 'POST':   
        form = Storeform(request.POST, request.FILES,instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:store'))
            
        else:
            message = generate_form_errors(form)
            form = Storeform()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance,
            
            }
    
        return render(request,'manager/store_add.html', context=context)



    else:
        form = Storeform(instance=instance)
        
        context = {
            "form": form,
            "instance": instance,
            
        }
        
    return render(request,'manager/store_add.html', context=context)






@allow_manager
@login_required(login_url='/login/')

def slider(request):
    instances = Slider.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/slider.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def slider_delete(request,id):
    instance = Slider.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:slider'))
@allow_manager
@login_required(login_url='/login/')
def slider_add(request,):
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slider'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/slider_add.html', context=context)



    else:
        form = SliderForm()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/slider_add.html', context=context)
@allow_manager
@login_required(login_url='/login/')
def slider_edit(request,id):
    instance = Slider.objects.get(id=id)
    if request.method == 'POST':   
        form = SliderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:slider'))
            
        else:
            message = generate_form_errors(form)
            form = SliderForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/slider_add.html', context=context)



    else:
        form = SliderForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/slider_add.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def food_categories(request):
    instances = FoodCategory.objects.all()
    
    context = {
        'instances': instances,
    }
    
    
    return render(request,'manager/food_categories.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def food_category_delete(request,id):
    instance = FoodCategory.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:food_categories'))

@allow_manager
@login_required(login_url='/login/')
def food_category_add(request,):
    if request.method == 'POST':   
        form = FoodCategoryform(request.POST, request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:food_categories'))
            
        else:
            message = generate_form_errors(form)
            form = FoodCategoryform()

            context = {
            "error": True,
            "message": message,
            "form": form,
            }
    
        return render(request,'manager/food_category_add.html', context=context)



    else:
        form = FoodCategoryform()
        
        context = {
            "form": form,
        }
        
    return render(request,'manager/food_category_add.html', context=context)

@allow_manager
@login_required(login_url='/login/')
def food_category_edit(request, id):
    instance = FoodCategory.objects.get(id=id)
    if request.method == 'POST':   
        form = FoodCategoryform(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:food_categories'))
            
        else:
            message = generate_form_errors(form)
            form = FoodCategoryform()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/food_category_add.html', context=context)



    else:
        form = FoodCategoryform(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/food_category_add.html', context=context)


@allow_manager
@login_required(login_url='/login/')

def food(request):
    instances = Food.objects.all()
    
    context = {
        'instances': instances,
    } 
    
    return render(request,'manager/food.html', context=context)

@allow_manager
@login_required(login_url='/login/')

def food_delete(request, id):
    instance = Food.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:food'))
@allow_manager
@login_required(login_url='/login/')

def food_add(request):
    if request.method == 'POST':   
        form = FoodForm(request.POST, request.FILES)
        foodcategory = request.POST.get('foodcategory')
        foodcategory = FoodCategory.objects.get(id=foodcategory)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.store = store
            instance.foodcategory = foodcategory    
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:food'))
        else:
            message = generate_form_errors(form)
            form = FoodForm()

            context = {
                "error": True,
                "message": message,
                "form": form,
            }
    
        return render(request, 'manager/food_add.html', context=context)
    else:
        form = FoodForm()
        
        context = {
            "form": form,
            
        }
        
    return render(request, 'manager/food_add.html', context=context)


@allow_manager
@login_required(login_url='/login/')
def food_edit(request, id):
    instance = Food.objects.get(id=id)
    if request.method == 'POST':   
        form = FoodForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:foods'))
            
        else:
            message = generate_form_errors(form)
            form = FoodForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/food_add.html', context=context)



    else:
        form = FoodForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/food_add.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def users(request):
    instances = User.objects.all()
    
    context = {
        'instances': instances,
    }
    
    return render(request,'manager/users.html', context=context)

@allow_manager
@login_required(login_url='/login/')

def users_delete(request, id):
    instance = User.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:users'))
@allow_manager
@login_required(login_url='/login/')

def users_add(request):
    if request.method == 'POST':   
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:users'))
        else:
            message = generate_form_errors(form)
            form = UserForm()

            context = {
                "error": True,
                "message": message,
                "form": form,
            }
    
        return render(request, 'manager/users_add.html', context=context)
    else:
        form = UserForm()
        
        context = {
            "form": form,
        }
        
    return render(request, 'manager/users_add.html', context=context)

@allow_manager
@login_required(login_url='/login/')
def users_edit(request, id):
    instance = User.objects.get(id=id)
    if request.method == 'POST':   
        form = UserForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:users'))
            
        else:
            message = generate_form_errors(form)
            form = UserForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/users_add.html', context=context)



    else:
        form = UserForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/users_add.html', context=context)

@allow_manager
@login_required(login_url='/login/')

def offers(request):
    instances = Offer.objects.all()
    
    context = {
        'instances': instances,
    }
    
    return render(request,'manager/offers.html', context=context)

@allow_manager
@login_required(login_url='/login/')

def offers_delete(request, id):
    instance = Offer.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:offers'))
@allow_manager
@login_required(login_url='/login/')

def offers_add(request):
    if request.method == 'POST':   
        form = OfferForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:offers'))
        else:
            message = generate_form_errors(form)
            form = OfferForm()

            context = {
                "error": True,
                "message": message,
                "form": form,
            }
    
        return render(request, 'manager/offers_add.html', context=context)
    else:
        form = OfferForm()
        
        context = {
            "form": form,
        }
        
    return render(request, 'manager/offers_add.html', context=context)

@allow_manager
@login_required(login_url='/login/')
def offers_edit(request, id):
    instance = Offer.objects.get(id=id)
    if request.method == 'POST':   
        form = OfferForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:offers'))
            
        else:
            message = generate_form_errors(form)
            form = OfferForm()

            context = {
            "error": True,
            "message": message,
            "form": form,
            "instance": instance
            }
    
        return render(request,'manager/offers_add.html', context=context)



    else:
        form = OfferForm(instance=instance)
        
        context = {
            "form": form,
            "instance": instance
        }
        
    return render(request,'manager/offers_add.html', context=context)
@allow_manager
@login_required(login_url='/login/')

def order(request):
    instances = Order.objects.all()
    
    context = {
        'instances': instances,
    }
    
    return render(request,'manager/order.html', context=context)

@allow_manager
@login_required(login_url='/login/')

def order_delete(request, id):
    instance = Order.objects.get(id=id)
    
    instance.delete()
    
    return HttpResponseRedirect(reverse('manager:order'))
@allow_manager
@login_required(login_url='/login/')

def order_add(request):
    if request.method == 'POST':   
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
            return HttpResponseRedirect(reverse('manager:order'))
        else:
            message = generate_form_errors(form)
            form = OrderForm()

            context = {
                "error": True,
                "message": message,
                "form": form,
            }
    
        return render(request, 'manager/order_add.html', context=context)
    else:
        form = OrderForm()
        
        context = {
            "form": form,
        }
        
    return render(request, 'manager/order_add.html', context=context)




    
