from django.db import models

class User(models.Model):
    
    user_nickname = models.CharField(primary_key=True, max_length=100, default='')
    user_name = models.CharField(max_length=150, default='')
    user_email = models.EmailField(default='')
    user_age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nickname: {self.user_nickname} | E-mail: {self.user_email}'

class Products(models.Model):

    name = models.CharField(max_length=150, default='')
    price = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    description = models.CharField(max_length=150, default='')

    class Meta:
        ordering = ['id']

class Sale(models.Model):

    total  = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    products = models.ManyToManyField(Products)

    class Meta:
        ordering = ['id']


   
