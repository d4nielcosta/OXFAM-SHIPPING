from django.contrib import admin
from manager.models import *

admin.site.register(Shop)
admin.site.register(Commodity, list_display=('name', 'ref_number', 'price', 'shop', ))
