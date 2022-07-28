from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View


class Signup(View):

    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
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
