from django.db import models
from django.conf import settings

class Location (models.Model):
    County = models.CharField (max_length = 20,null=True)
    City_or_Town = models.CharField (max_length = 20,null=True)
    Area_name = models.CharField (max_length = 20,null=True)

    def __str__(self):
        return "%s/%s/%s" %(self.County,self.City_or_Town,self.Area_name)

class RealEstateManagementAgency (models.Model):
    Agency_name = models.CharField (max_length = 50,null=True)
    Phone_number = models.IntegerField (null=True)
    Email_address = models.EmailField (null=True)
    Website = models.CharField (max_length = 50,null=True)
    Office_location = models.ForeignKey (Location,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return "%s" %(self.Agency_name)

class SuperAdministrator (models.Model):
    User_details = models.OneToOneField (settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    Agency_details = models.ForeignKey (RealEstateManagementAgency,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return "%s/%s" %(self.Agency_details.Agency_name,self.User_details.first_name)

class Administrator (models.Model):
    User_details = models.OneToOneField (settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    Agency_details = models.ForeignKey (RealEstateManagementAgency,on_delete = models.CASCADE,null = True)

    def __str__(self):
        return "%s/%s" %(self.Agency_details.Agency_name,self.User_details.first_name)

class Tenant (models.Model):
    User_details = models.ForeignKey (settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    Entry_date = models.DateTimeField (null = True)
    Rent_payment_date = models.DateTimeField (null = True)
    Amount_paid = models.IntegerField(default = 0)
    Current_month_payment_status = models.BooleanField (default = False)

    def __str__(self):
        return "%s" %(self.User_details.first_name)

class Avatar (models.Model):
    User_details = models.OneToOneField (settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True)
    avatar = models.FileField (null=True)

classNames = {
    'AgencyClass' : RealEstateManagementAgency,
    'SuperAdministratorClass' : SuperAdministrator,
    'AdministratorClass' : Administrator,
    'TenantClass' : Tenant,
    'LocationClass' : Location,
    'Avatar' : Avatar
  }

agency_class = RealEstateManagementAgency
superadmin_class = SuperAdministrator
admin_class = Administrator
tenant_class = Tenant
location_class = Location
avatar_class = Avatar
