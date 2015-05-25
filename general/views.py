from django.shortcuts import render
from models import *

# Create your views here.

def index(request):
    context_dict = {}

    textWrapper = Text.objects.get(id=1)

    context_dict['intro'] = textWrapper.intro
    context_dict['mission'] = textWrapper.mission
    context_dict['description'] = textWrapper.description
    context_dict['volunteerText'] = textWrapper.volunteer
    context_dict['donate'] = textWrapper.donate
    context_dict['address'] = textWrapper.location
    context_dict['footerdonate'] = textWrapper.footerdonate
    print context_dict

    return render(request, 'index.html', context_dict)