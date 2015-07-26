import datetime

from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=128)
    oxfamID = models.CharField(max_length=10, primary_key=True)
    telephone = models.TextField()
    email = models.EmailField(blank=True, default="")
    addressL1 = models.TextField(blank=False, default="")
    addressL2 = models.TextField(blank=True)
    postcode = models.CharField(max_length=10)

    randomletter = models.CharField(max_length=1)

    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Commodity(models.Model):
    ref_number = models.CharField(max_length=128, primary_key=True)
    name = models.CharField(max_length=128)
    shop = models.ForeignKey(Shop)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    comments = models.TextField(max_length=300, blank=True, default="")
    date_added = models.DateTimeField(auto_now=True, auto_now_add=True, default=datetime.date.today())

    def save(self, *args, **kwargs):
        super(Commodity, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Commodities"
