from django.db import models
from .product import Product
from .customer import Customer
import datetime
from .category import Category


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now)
    address = models.CharField(default='N/A', max_length=500)
    phone = models.CharField(default='N/A',max_length=10)
    status = models.BooleanField(default=False)

    def placeorder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer):
        return Order.objects.filter(customer = customer)

