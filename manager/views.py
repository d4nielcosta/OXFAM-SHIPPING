from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from manager.models import Shop
from manager.models import Commodity
# Create your views here.

def manager(request):
    context_dict = {}
    return render(request, 'manager_base.html', context_dict)

def storerank(request):
    return render(request, 'manager/index.html')

def allstores(request):
        # Get all the shops in the database and add an attribute
    # nwname which is a modified version of the shop's name
    # without whitespace
    shop_list = Shop.objects.all()
    for shop in shop_list:
        shop.nwname = shop.name.replace(' ', '_')
    
    # For every shop get the associated commodities and
    # also add to every commodity a nwname attribute as well
    shops_and_commodities = []
    for shop in shop_list:
        comm_list = Commodity.objects.filter(shop=shop)
        for cmd in comm_list:
            cmd.nwname = cmd.name.replace(' ', '_')
        shop_index = []
        shop_index.append(shop)
        shop_index.append(comm_list)
        shops_and_commodities.append(shop_index)

    context_dict = {'shops_and_commodities': shops_and_commodities}

    return render(request, 'manager/allstores.html', context_dict)


def index(request):
    return render(request, 'manager/index.html')

def dev(request):
    return render(request, 'manager/dev.html')