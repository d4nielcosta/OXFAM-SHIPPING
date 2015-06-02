from django.shortcuts import render

# Create your views here.

def manager(request):
    context_dict = {}

    return render(request, 'manager.html', context_dict)