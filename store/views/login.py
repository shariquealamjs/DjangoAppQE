from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(email, password)

        customer = Customer.get_customer_by_email(email)

        if customer:
            encryptedpassword = customer.password
            flag = check_password(password, encryptedpassword)
            if flag:
                request.session['customer_email'] = customer.email
                request.session['customer_id'] = customer.id
                return redirect('homepage')
            else:
                return HttpResponse('Email or Password is wrong!')
        else:
            return HttpResponse('Email or Password is wrong!')
