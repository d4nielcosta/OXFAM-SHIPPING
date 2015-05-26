from django.shortcuts import render
from datetime import date
from models import *
import calendar
# Create your views here.

def index(request):
    context_dict = {}

    # Add valid days
    context_dict['v_days'] = list(range(1,32))
    # Add valid months
    context_dict['v_months'] = list(calendar.month_name)[1:]
    # Add valid years starting this year
    context_dict['v_years'] = list(
                              reversed(
                              range(1900, int(date.today().year) + 1)))

    if request.method == 'POST':
        forename = request.POST.get('forename', '')
        surname = request.POST.get('surname', '')
        primephone = request.POST.get('pphone', '')
        secphone = request.POST.get('sphone', '')
        address = request.POST.get('address', '')
        role = request.POST.get('role', '')
        bday = request.POST.get('selbday', '')
        bmonth = request.POST.get('selbmonth', '')
        byear = request.POST.get('selbyear', '')

        #black magic
        validmonth = dict((v,k) for k,v in enumerate(calendar.month_abbr))[bmonth[:3]]
        preproccdate = str(byear) + "-" + str(validmonth) + "-" + bday
        bdate = datetime.datetime.strptime(preproccdate, "%Y-%m-%d")
        #-----------

        parentalPerm = request.POST.get('parentalPerm', '') == 'on'
        workPermission = request.POST.get('workPermission', '') == 'on'

        print "Forename: " + forename
        print "Surname: " + surname
        print "Primary phone: " + primephone
        print "Secondary phone: " + secphone
        print "Role: " + role
        print "address: " + address
        print "Date of birth: " + preproccdate

        volApp = VolunteerApplication.objects.create(
            forename=forename,
            surname=surname,
            primary_phone=primephone,
            secondary_phone=secphone,
            role=role,
            address=address,
            dob=bdate)
        volApp.save()

        print "application saved"
    try:
        textWrapper = Text.objects.get(id=1)

        context_dict['intro'] = textWrapper.intro
        context_dict['mission'] = textWrapper.mission
        context_dict['description'] = textWrapper.description
        context_dict['volunteerText'] = textWrapper.volunteer
        context_dict['donate'] = textWrapper.donate
        context_dict['address'] = textWrapper.location
        context_dict['footerdonate'] = textWrapper.footerdonate
        print context_dict
    except:
        pass

    return render(request, 'index.html', context_dict)