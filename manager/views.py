from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from manager.models import Shop

# Create your views here.

def manager(request):
    context_dict = {}
    return render(request, 'manager.html', context_dict)

def storerank(request):
    return render(request, 'manager/index.html')

def allstores(request):
    shop_list = Shop.objects.all()
    context_dict = {'shops': shop_list}
    for shop in shop_list:
        shop.nwname = shop.name.replace(' ', '_');
    
    return render(request, 'manager/allstores.html', context_dict)

def index(request):
    return render(request, 'manager/index.html')

def dev(request):
    return render(request, 'manager/dev.html')