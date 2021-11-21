from django.db import models

# Create your models here.

class Companies(models.Model):
    name = models.CharField(max_length=250)
    phn = models.CharField(max_length=10)
    quantity = models.CharField(max_length=250)
    billing_street = models.CharField(max_length=250)
    billing_city = models.CharField(max_length=250)
    billing_state = models.CharField(max_length=250)
    billing_country = models.CharField(max_length=250)




class Client(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    choices = {
        ('Umbrella','Umbrella'),
        ('Clampett Oil and Gas Corp','Clampett Oil and Gas Corp'),
        ('Gas','Gas'),
        ('Milk','Milk'),
        ('Pipes','Pipes'),
        ('Bamboo','Bamboo'),

    }
    company = models.CharField(max_length=250, choices=choices, default='1')
    qty = models.CharField(max_length=50)
    address = models.CharField(max_length=250)