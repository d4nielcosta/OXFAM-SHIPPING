__author__ = 'daniel'

from django.core.mail import send_mail
from django.conf import settings

def send_email_confirmation(volapp):
    subject = 'OXFAM - Thank you for applying to volunteer with us.'
    from_email = settings.EMAIL_HOST_USER
    to_list = [volapp.email]
    message = \
        "Hi. Thank you for applying to volunteer with us. We will get in touch with you as soon as possible. \n " \
        "In the meanwhile, here's a copy of your application: \n \n \n " \
        "PERSONAL DETAILS \n" \
        "------------" "\n" \
        "Forename: " + volapp.forename + "\n" \
        "Surname: " + volapp.surname + "\n" \
        "Email: " + volapp.email + "\n" \
        "Primary Phone: " + volapp.primary_phone + "\n" \
        "Secondary Phone: " + volapp.secondary_phone + "\n" \
        "Date of Birth: " + volapp.dob.strftime('%d/%m/%Y') + "\n" \
        "Address \n" + \
            volapp.address + "\n \n "\
        "PERMISSION TO WORK \n" \
        "------------" "\n" \
        "       In the UK (goverment): " + str(volapp.permission_to_work) + "\n" \
        "       Parental Permission (if minor): " + str(volapp.parental_permission) + "\n" \
        "\n" \
        "EMERGENCY CONTACT" + "\n" \
        "------------" "\n" \
        "       Name: " + volapp.emergency_contact_forename + " " + volapp.emergency_contact_surname + "\n" \
        "       Phone Number: " + volapp.emergency_contact_phone + "\n" \
        "\n" \
        "REFERENCES" + "\n" \
        "------------" "\n" \
        "       Forename: " + volapp.reference1_forename + "\n" \
        "       Surname: " + volapp.reference1_surname + "\n" \
        "       Phone: " + volapp.reference1_primary_phone + "\n" \
        "       Email: " + volapp.reference1_email + "\n" \
        "\n" \
        "       Forename: " + volapp.reference2_forename + "\n" \
        "       Surname: " + volapp.reference2_surname + "\n" \
        "       Phone: " + volapp.reference2_primary_phone + "\n" \
        "       Email: " + volapp.reference2_email + "\n" \
        "\n \n"\
        "If you find any problems with your application please contact us as soon as possible. \n \n" \
        "Best Regards, \n The Oxfam Team"

    send_mail(subject, message, from_email, to_list, fail_silently=False)

def send_application_email(volapp):
    subject = 'NEW Volunteer Application'
    from_email = settings.EMAIL_HOST_USER
    to_list = ["danielcosta@gmx.com"]
    message = \
        "Application to volunteer in the shipping centre: " \
        " \n \n \n " \
        "PERSONAL DETAILS \n" \
        "------------" "\n" \
        "Forename: " + volapp.forename + "\n" \
        "Surname: " + volapp.surname + "\n" \
        "Email: " + volapp.email + "\n" \
        "Primary Phone: " + volapp.primary_phone + "\n" \
        "Secondary Phone: " + volapp.secondary_phone + "\n" \
        "Date of Birth: " + volapp.dob.strftime('%d/%m/%Y') + "\n" \
        "Address \n" + \
            volapp.address + "\n \n "\
        "PERMISSION TO WORK \n" \
        "------------" "\n" \
        "       In the UK (goverment): " + str(volapp.permission_to_work) + "\n" \
        "       Parental Permission (if minor): " + str(volapp.parental_permission) + "\n" \
        "\n" \
        "EMERGENCY CONTACT" + "\n" \
        "------------" "\n" \
        "       Name: " + volapp.emergency_contact_forename + " " + volapp.emergency_contact_surname + "\n" \
        "       Phone Number: " + volapp.emergency_contact_phone + "\n" \
        "\n" \
        "REFERENCES" + "\n" \
        "------------" "\n" \
        "       Forename: " + volapp.reference1_forename + "\n" \
        "       Surname: " + volapp.reference1_surname + "\n" \
        "       Phone: " + volapp.reference1_primary_phone + "\n" \
        "       Email: " + volapp.reference1_email + "\n" \
        "\n" \
        "       Forename: " + volapp.reference2_forename + "\n" \
        "       Surname: " + volapp.reference2_surname + "\n" \
        "       Phone: " + volapp.reference2_primary_phone + "\n" \
        "       Email: " + volapp.reference2_email + "\n" \
        "\n \n"\
        "Best Regards, \n The Oxfam Team"

    send_mail(subject, message, from_email, to_list, fail_silently=False)
