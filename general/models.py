import datetime
from django.db import models
from django.core.validators import RegexValidator

#Validators
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:'+999999999")

class Text(models.Model):
    id = models.IntegerField(primary_key=True, default=1) # Variable for flexibility in future updates
    intro = models.TextField()
    mission = models.TextField()
    description = models.TextField()
    volunteer = models.TextField()
    donate = models.TextField()
    footerdonate = models.TextField()
    location = models.TextField()

# class Store(models.Model):
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length=256)
#     email = models.EmailField()
#     phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
#     manager = models.CharField(max_length=256)
#
#     #Composite Address
#     address = models.TextField()
#     postcode= models.CharField(max_length=5)
#
#     def __unicode__(self):
#         return self.id
#
#
#
# class Commodity(models.Model):
#     id = models.IntegerField(primary_key=True, unique=True)
#     name = models.CharField(max_length=256)
#     description = models.TextField()
#     price = models.IntegerField()
#     date = models.DateField(auto_now=True)
#     shop = models.ForeignKey(Store)


class VolunteerApplication(models.Model):

    forename = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    role = models.TextField()

    dob = models.DateField()

    parental_permission = models.BooleanField(default=False)
    permission_to_work = models.BooleanField(default=False)


    #emergency contact
    emergency_contact_forename = models.CharField(max_length=128, default="NO FORENAME ENTERED")
    emergency_contact_surname = models.CharField(max_length=128, default="NO SURNAME ENTERED")
    emergency_contact_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)

    address = models.TextField(max_length=300, blank=True, default="")
    # reference1
    reference1_forename = models.CharField(max_length=128, blank=True, default="")
    reference1_surname = models.CharField(max_length=128, blank=True, default="")
    reference1_primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference1_secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference1_email = models.EmailField(blank=True, default="")


    # reference2
    reference2_forename = models.CharField(max_length=128, blank=True, default="")
    reference2_surname = models.CharField(max_length=128, blank=True, default="")
    reference2_primary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference2_secondary_phone = models.CharField(validators=[phone_regex], blank=True, max_length=15)
    reference2_email = models.EmailField(blank=True, default="")

    def save(self, *args, **kwargs):
        super(VolunteerApplication, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.forename + ' ' + self.surname
        #make sure to modify admin so it shows column with birthday and date joined

