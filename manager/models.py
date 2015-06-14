from django.db import models

# Create your models here.

class Shop(models.Model):
    oxfamID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, default="")
    addressL1 = models.TextField(blank=False, default="")
    addressL2 = models.TextField(blank=True, default="")
    postcode = models.CharField(max_length=10, blank=False)


    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
