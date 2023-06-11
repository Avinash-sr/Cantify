from django.db import models
from django.contrib.auth.models import User
from canteen_app.models import Item

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrollment_no = models.CharField(max_length=11, unique=True, primary_key=True)
    batch = models.CharField(max_length=255)

    def __str__(self):
       return self.enrollment_no

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.item.name+str(self.quantity))
    

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    order_id = models.CharField(default="", max_length=500)
    cart  = models.ForeignKey(Cart,on_delete=models.CASCADE,default=None)
    # quantity = models.IntegerField(default=1)
    placed_on = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id
