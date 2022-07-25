from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer


def index(request):
    products = Product.get_all_products()
    categories = Category.get_all_categories()
    print(request.GET)
    categoryid = request.GET.get('category ')
    print("Category ID is:", categoryid)
    # if categoryid:
    #    products = Product.get_products_by_id()
    # else:
    #    products = Product.get_all_products()

    if categoryid:
        data = {'products': Product.get_products_by_id(categoryid)}
        print("Dear Customer, your email is: ",request.session.get('customer_email'))
        print("Dear Customer, your id is: ", request.session.get('customer_id'))
    else:
        data = {'categories': categories}
        print("Dear Customer, your email is: ",request.session.get('customer_email'))
        print("Dear Customer, your id is: ", request.session.get('customer_id'))

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

        # Validation
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        if not first_name:
            error_message = "First Name required!"
        elif len(first_name) < 4:
            error_message = "First name must be of minimum 4 character length!"
        if not last_name:
            error_message = "Last Name required!"
        elif len(last_name) < 3:
            error_message = "Last name must be of minimum 3 character length!"
        if not phone:
            error_message = "Phone Number is required!"
        elif len(phone) < 10:
            error_message = "Phone must consist 10 digits!"
        elif len(phone) > 10:
            error_message = "Phone can have maximum 10 digits!"
        elif customer.isexist():
            error_message = "This email is already registered. "
        # Saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
        else:
            return render(request, 'signup.html', {'error': error_message})

        return HttpResponse('Sign Up Success')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)

        customer = Customer.get_customer_by_email(email)
        encryptedpassword = customer.password
        if customer:
            flag = check_password(password, encryptedpassword)
            if flag:
                request.session['customer_email']=customer.email
                request.session['customer_id'] = customer.id
                return redirect('homepage')
            else:
                return HttpResponse('Email or Password is wrong!')
        else:
            return HttpResponse('Email or Password is wrong!')


