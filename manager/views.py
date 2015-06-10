from django.shortcuts import render

from manager.models import Shop

# Create your views here.

def manager(request):
    context_dict = {}
    return render(request, 'manager.html', context_dict)


def storerank(request):
    shop_list = Shop.objects.all()
    context_dict = {'shops': shop_list}

    return render(request, 'saleslog.html', context_dict)

def index(request):

    return render(request, 'manager/index.html')