from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(blank=True, upload_to='items', default='/items/default_item.jpg')

    def __str__(self):
        return self.name