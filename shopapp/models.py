from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Products(models.Model):
    # class Meta:
    #     ordering = ["name", "price"]

    name = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    discount = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)

    # @property
    # def description_short(self):
    #     if len(self.description)<48:
    #         return self.description
    #     return self.description[:48]+"..."

    def __str__(self):
        return f"Products(pk={self.pk},name={self.name!r})" # как ссылки


class Order(models.Model):
    # class Meta:
    #     ordering = ["user", "products"]
    delivery_address = models.TextField(null=True, blank=True)
    promocode = models.CharField(max_length=16, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    products = models.ManyToManyField(Products, related_name="orders")