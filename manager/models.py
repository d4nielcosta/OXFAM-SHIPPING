from django.db import models
import datetime
# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, default="")
    address = models.TextField(max_length=300, blank=True, default="")

    def save(self, *args, **kwargs):
        super(Shop, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Commodity(models.Model):
	name = models.CharField(max_length=128)
	shop = models.ForeignKey(Shop)
	price = models.DecimalField(max_digits=16, decimal_places=2)
	comments = models.TextField(max_length=300, blank=True, default="")
	date_added = models.DateTimeField(auto_now=True, auto_now_add=True, default=datetime.date.today());

	def save(self, *args, **kwargs):
		super(Commodity, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Commodities"