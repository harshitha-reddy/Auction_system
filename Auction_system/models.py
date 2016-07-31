from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db import models
from time import time
from PIL import Image

# Create your models here.
def getImage(instance, filename):
    return "auction_system/image_{0}_{1}".format(str(time()),filename)


class product(models.Model):
    name=models.CharField(max_length=100)
    price = models.CharField(max_length=10)
    category=models.CharField(max_length=10)
    description=models.TextField(max_length=100)
    createdby=models.ForeignKey(User)
    noitem = models.IntegerField()
    purdate = models.DateField(default=None)
    created=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to=getImage)

    def __unicode__(self):
        return self.name

class Seller(models.Model):
    username = models.ForeignKey(User)
    product_id=models.ForeignKey(product)
    created=models.DateTimeField(auto_now_add=True)



    def __unicode__(self):
        return self.name

class Buyer(models.Model):
    username = models.ForeignKey(User)
    product_id=models.ForeignKey(product)
    price=models.CharField(max_length=10)
    created=models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.username
