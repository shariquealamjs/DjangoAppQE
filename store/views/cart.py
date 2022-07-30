from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


class Cart(View):

    def get(self, request):
        id = list(request.session.get('cart').keys())
        products_in_cart = Product.get_products_using_product_id(id)
        print(request.session.get('cart'))

        return render(request, 'cart.html', {'products_in_cart':products_in_cart})
