from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View


class Index(View):

    def get(self, request):
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
            print("Dear Customer, your email is: ", request.session.get('customer_email'))
            print("Dear Customer, your id is: ", request.session.get('customer_id'))
        else:
            data = {'categories': categories}
            print("Dear Customer, your email is: ", request.session.get('customer_email'))
            print("Dear Customer, your id is: ", request.session.get('customer_id'))

        return render(request, 'index.html', data)

    def post(self, request):
        categoryid = request.GET.get('category ')
        data = {'products': Product.get_products_by_id(categoryid)}

        product = request.POST.get('product')
        cart = request.session.get('cart')

        print(categoryid,product,cart)

        if cart:
            quantity = cart.get(product)
            print(quantity)
            if quantity:
                cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:

            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return render(request, 'index.html', data)
