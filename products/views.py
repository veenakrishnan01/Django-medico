from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    products =  Product.objects.all()
    return render(request, 'retrieve.html', {'product_list':products})


@login_required(login_url='/login/')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm()
    return render(request, 'create.html', {'form': form})

@login_required(login_url='/login/')
def product_read(request):
    product_list = Product.objects.all()
    search_term = request.GET.get('search')
    if search_term:
        product_list = product_list.filter(name__istartswith=search_term)
    return render(request,'retrieve.html',{'product_list':product_list})

@login_required(login_url='/login/')
def product_update(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('retrieveproduct')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})

# @login_required(login_url='/login/')
# def product_delete(request,pk):
#     product=Product.objects.get(pk=pk)  
#     if request.method == 'POST':
#         product.delete()
#         return redirect('retrieveproduct')
    
#     return render(request,'retrieve.html',{'product':product})

@login_required(login_url='/login/')
def product_delete(request,pk):
    value=Product.objects.get(pk=pk)  
    if request.method == 'POST':
        value.delete()
        return redirect('retrieveproduct')
    
    return render(request,'retrieve.html',{'product': value})
