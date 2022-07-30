from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.order import Order


class Checkout(View):
    def post(self, request):
        print(request.POST)
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_products_using_product_id(list(cart.keys()))

        print(cart, products)

        for product in products:
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.placeorder()

            request.session['cart'] = {}
        return redirect('cart')
