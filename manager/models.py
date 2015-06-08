from django.db import models

# Create your models here.
class Shop(models.Model):
	name = models.CharField(max_length=128)
	email = models.EmailField(blank=True, default="")
	address = models.TextField(max_length=300, blank=True, default="")

	def save(self, *args, **kwargs):
		super(Shop, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.name