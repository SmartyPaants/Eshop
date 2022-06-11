from django.http import HttpResponse
from django.shortcuts import render, redirect
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

        # Validations
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email' : email
        }

        error_message = None

        customer = Customer(first_name = first_name, 
                                last_name = last_name, 
                                phone = phone, 
                                email = email, 
                                password = password)

        if not first_name:
            error_message = "First Name Required!!"
        elif len(first_name) < 4:
            error_message = "First Name Should Be At Least 4 Characters Long!!"
        elif not last_name:
            error_message = "Last Name Required!!"
        elif len(last_name) < 4:
            error_message = "Last Name Should Be At Least 4 Characters Long!!"
        elif not phone:
            error_message = "Phone Number Requried!!"
        elif len(phone) < 10:
            error_message = "Phone Number Should Be At Least 10 Digits Long!!"
        elif len(password) < 6:
            error_message = "Password Should Be At Least 6 Characters Long!!"
        elif len(email) < 5:
            error_message = "Email Should Be At Least 5 Characters Long!!"
        elif customer.isExists():
            error_message = 'Email is already used...'

        # Saving
        if not error_message:
            print(first_name, last_name, phone, email, password)
            

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error' : error_message,
                'values' : value
            }
            return render(request, 'signup.html', data)