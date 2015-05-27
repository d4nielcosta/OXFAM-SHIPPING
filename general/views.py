from django.shortcuts import render
from datetime import date
from models import *
import calendar
# Create your views here.

def getDateTimeField(day, month, year):
    validmonth = dict((v,k) for k,v in enumerate(calendar.month_abbr))[month[:3]]
    preproccdate = str(year) + "-" + str(validmonth) + "-" + day
    return datetime.datetime.strptime(preproccdate, "%Y-%m-%d")

def index(request):
    context_dict = {}

    # Initialize the registration step on first visit
    if 'rgstr_step' not in request.session:
        request.session.flush()
        request.session['rgstr_step'] = 0

    # The client requested to go back in the registration from
    if request.method == 'POST' and request.POST.get('back', 0) == "yes":
        request.session['rgstr_step'] -= 1

    # Data extraction from first part of registration
    elif request.method == 'POST' and request.session['rgstr_step'] == 0:
        request.session['forename'] = request.POST.get('forename', '')
        request.session['surname'] = request.POST.get('surname', '')
        request.session['primary_phone'] = request.POST.get('pphone', '')
        request.session['secondary_phone'] = request.POST.get('sphone', '')
        request.session['address'] = request.POST.get('address', '')
        request.session['bday'] = request.POST.get('selbday', '')
        request.session['bmonth'] = request.POST.get('selbmonth', '')
        request.session['byear'] = request.POST.get('selbyear', '')

        request.session['rgstr_step'] += 1
    
    # Data extraction from second part of registration
    elif request.method == 'POST' and request.session['rgstr_step'] == 1:
        request.session['em_forename'] = request.POST.get('em_forename', '')
        request.session['em_surname'] = request.POST.get('em_surname', '')
        request.session['em_phone'] = request.POST.get('em_phone', '')

        request.session['rgstr_step'] += 1

    # Data extraction from third part of registration
    elif request.method == 'POST' and request.session['rgstr_step'] == 2:
        request.session['fr_forename'] = request.POST.get('fr_forename', '')
        request.session['fr_surname'] = request.POST.get('fr_surname', '')
        request.session['fr_pphone'] = request.POST.get('fr_pphone', '')
        request.session['fr_sphone'] = request.POST.get('fr_sphone', '')
        request.session['fr_email'] = request.POST.get('fr_email', '')

        request.session['rgstr_step'] += 1

    # Data extraction from fourth part of registration
    elif request.method == 'POST' and request.session['rgstr_step'] == 3:
        request.session['sr_forename'] = request.POST.get('sr_forename', '')
        request.session['sr_surname'] = request.POST.get('sr_surname', '')
        request.session['sr_pphone'] = request.POST.get('sr_pphone', '')
        request.session['sr_sphone'] = request.POST.get('sr_sphone', '')
        request.session['sr_email'] = request.POST.get('sr_email', '')

        request.session['rgstr_step'] += 1

    elif request.method == 'POST' and request.session['rgstr_step'] == 4:
        request.session['par_perm'] = request.POST.get('par_perm') == 'on'
        request.session['work_perm'] = request.POST.get('work_perm') == 'on'
        request.session['rgstr_step'] += 1

    elif request.method == 'POST' and request.session['rgstr_step'] == 5:
        bday = getDateTimeField(request.session['bday'],
                                request.session['bmonth'],
                                request.session['byear'])
        volapp = VolunteerApplication.objects.create(
            forename=request.session['forename'],
            surname=request.session['surname'],
            primary_phone=request.session['primary_phone'],
            secondary_phone=request.session['secondary_phone'],
            dob=bday,
            parental_permission=request.session['par_perm'],
            permission_to_work=request.session['work_perm'],
            emergency_contact_forename=request.session['em_forename'],
            emergency_contact_surname=request.session['em_surname'],
            emergency_contact_phone=request.session['em_phone'],
            address=request.session['address'],
            reference1_forename=request.session['fr_forename'],
            reference1_surname=request.session['fr_surname'],
            reference1_primary_phone=request.session['fr_pphone'],
            reference1_secondary_phone=request.session['fr_sphone'],
            reference1_email=request.session['fr_email'],
            reference2_forename=request.session['sr_forename'],
            reference2_surname=request.session['sr_surname'],
            reference2_primary_phone=request.session['sr_pphone'],
            reference2_secondary_phone=request.session['sr_sphone'],
            reference2_email=request.session['sr_email'])
        
        volapp.save()
        print "Volunteer Application saved"
        request.session.flush()
        request.session['rgstr_step'] = 0
        
    
    if request.session['rgstr_step'] != 0:
        context_dict['forename'] = request.session['forename']

    # Add registration step in context dict
    context_dict['rgstr_step'] = request.session['rgstr_step']
    context_dict['rgstr_perc'] = request.session['rgstr_step'] * 20
    # Add valid days
    context_dict['v_days'] = list(range(1,32))
    # Add valid months
    context_dict['v_months'] = list(calendar.month_name)[1:]
    # Add valid years starting this year
    context_dict['v_years'] = list(
                              reversed(
                              range(1900, int(date.today().year) + 1)))

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