from django.db import models
from django.contrib.auth.models import User
from product.models import product

class OrderStatus(models.TextChoices):
    PROCESSING = 'processing', 'Processing'
    DELIVERED = 'delivered', 'Delivered'
    SHIPPED = 'shipped', 'Shipped'
  
class PaymentStatus(models.TextChoices):
    PAY = 'pay', 'Pay'
    PAID = 'paid', 'Paid'
    
class PaymentMethod(models.TextChoices):
    CASH = 'cash', 'Cash'
    CARD = 'card', 'Card'

class Order(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    order_status = models.CharField(max_length=50, choices=OrderStatus.choices, default=OrderStatus.PROCESSING)
    payment_status = models.CharField(max_length=50, choices=PaymentStatus.choices, default=PaymentStatus.PAY)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices, default=PaymentMethod.CASH)
    created_at = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=50, blank=False)
    street = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=50, blank=False)
    postal_code = models.CharField(max_length=50, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

class OrderItem(models.Model):
    product = models.ForeignKey(product, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE, related_name="order_items")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    name = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
