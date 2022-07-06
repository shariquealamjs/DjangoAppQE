from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    print(request.GET)
    categoryid = request.GET.get('category ')
    print("Category ID is:",categoryid)
    # if categoryid:
    #    products = Product.get_products_by_id()
    # else:
    #    products = Product.get_all_products()

    if categoryid:
        data = {'products' : Product.get_products_by_id(categoryid)}
    else:
        data = {'categories': categories}
    return render(request, 'index.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    if request.method == 'POST':
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        phone = postdata.get('phone')
        email = postdata.get('email')
        password = postdata.get('password')

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)

        customer.register()

        return HttpResponse('Sign Up Success')
