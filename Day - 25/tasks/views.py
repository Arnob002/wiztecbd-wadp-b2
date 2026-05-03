from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from tasks.models import *
from tasks.forms import *
from decimal import Decimal

def register_page(request):
     if request.method=="POST":
        username=request.POST.get('username')
        full_name=request.POST.get('full_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        conf_password=request.POST.get('conf_password')
        
        if password == conf_password:
            CreateInfoModel.objects.create_user(
                username=username,
                full_name=full_name,
                password=password,
                email=email,
            )
            return redirect('login_page')

     return render(request,'register.html')

def login_page(request):
     if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user:
            login(request,user)
            return redirect('home_page')
        else:
            print("Invalid")        

     return render(request,'login.html')

@login_required
def logout_page(request):
    logout(request)

    return redirect('login_page')

@login_required
def home_page(request):

    return render(request,'home.html')

def task_list(request):

    return render(request,"task-list.html")

def user_profile(request):

    return render(request,'profile.html')

def update_profile(request):
    try:
        user_data = request.user.user_profile
    except ProfileModel.DoesNotExist:
        user_data = None

    if request.method == 'POST':
        form_data = UpdateProfileForm(request.POST,request.FILES,instance=user_data)

        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('user_profile')
    

    form_data = UpdateProfileForm(instance =user_data)
    context = {
        'form_data' : form_data,
        'form_title' : 'Update profile info',
        'form_btn' : "update",

    }
    
    return render(request,'master/base-form.html',context)

def product_list(request):
    product_data = ProductModel.objects.all()

    context = {
        'product_data' : product_data
    }

    return render(request,'product-list.html',context)

def add_product(request):
    if request.method == 'POST':
        form_data = ProductForm(request.POST)
        if form_data.is_valid():
            form_data = form_data.save(commit=False)
            form_data.created_by = request.user
            form_data.total_amount = form_data.price * form_data.qty
            form_data.save()
            return redirect('product_list')

    form_data = ProductForm()

    context = {
        'form_data' : form_data,
        'form_title' : 'Add Product info',
        'form_btn' : 'add product',
    }

    return render(request,'master/base-form.html',context)