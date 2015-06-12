from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from manager.models import Shop

# Create your views here.

@login_required
def manager(request):
    context_dict = {}
    return render(request, 'manager.html', context_dict)

@login_required
def storerank(request):
    shop_list = Shop.objects.all()
    context_dict = {'shops': shop_list}

    return render(request, 'saleslog.html', context_dict)

@login_required
def index(request):
    return render(request, 'manager/index.html')

@login_required
def dev(request):
    return render(request, 'manager/dev.html')