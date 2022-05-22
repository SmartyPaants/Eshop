from django.http import HttpResponse
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_id(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(first_name, last_name, phone, email, password)
        customer = Customer(first_name = first_name, 
                            last_name = last_name, 
                            phone = phone, 
                            email = email, 
                            password = password)
        
        customer.register()
        return HttpResponse("Signup Successful")