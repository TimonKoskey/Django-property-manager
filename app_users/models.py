from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

ROLE_CHOICES = (
    ("super-administrator", "super-administrator"),
    ("administrator", "administrator"),
    # ("Tenant", "Tenant")
)

PAYMENT_STATUS=(
    ("complete payment", "complete payment"),
    ("incomplete payment", "incomplete payment"),
    ("unpayed", "unpayed")
)

class Location (models.Model):
    county = models.CharField(max_length=20)
    city_or_town = models.CharField(max_length=20)
    area_or_estate_name = models.CharField(max_length=20, null=True, blank=True)
    street_name = models.CharField(max_length=20, null=True, blank=True)
    buiding_name = models.CharField(max_length=20, null=True, blank=True)

class ManagementCompanyDetail (models.Model):
    company_name = models.CharField(max_length=20)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    phone_number = models.IntegerField()
    physical_address = models.CharField(max_length=20)

class Role (models.Model):
    role_name = models.CharField(max_length = 20,choices=ROLE_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)
    # management_company_name = models.ForeignKey(ManagementCompanyDetail, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s" %(self.role_name)

class ManagementPersonelDetails (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    role_name = models.CharField(max_length = 20,choices=ROLE_CHOICES, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)
    mobile_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "%s - %s" %(self.user,self.role_name)

class TenantDetail (models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=30, blank=True, null=True)
    relationship_status = models.CharField(max_length=10, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=20, blank=True, null=True)
    emergency_contact_phone_number = models.IntegerField(blank=True, null=True)

class TenantsRecord (models.Model):
    tenant = models.ForeignKey(TenantDetail, on_delete=models.CASCADE, blank=True, null=True)
    unit_contenttype = models.ForeignKey(ContentType,on_delete = models.CASCADE,null=True,blank=True)
    unit_object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey('unit_contenttype', 'unit_object_id')
    date_of_entry = models.DateTimeField(auto_now_add=True)
    date_of_exit = models.DateTimeField(null=True,blank=True)

class TenantPaymentRecord (models.Model):
    tenant_record_obj = models.ForeignKey(TenantsRecord, on_delete=models.CASCADE, blank=True, null=True)
    expected_amount = models.IntegerField(null=True,blank=True)
    amount_paid = models.IntegerField(null=True,blank=True)
    balance = models.IntegerField(null=True,blank=True)
    mode_of_payment = models.CharField(max_length=30,null=True,blank=True);
    date_of_payment = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS,null=True,blank=True)
    unit_contenttype = models.ForeignKey(ContentType,on_delete = models.CASCADE,null=True,blank=True)
    unit_object_id = models.PositiveIntegerField(null=True,blank=True)
    content_object = GenericForeignKey('unit_contenttype', 'unit_object_id')



location_class = Location
company_management_class = ManagementCompanyDetail
role_class = Role
user_detail_class = ManagementPersonelDetails
tenant_details_class = TenantDetail
tenants_record_class = TenantsRecord
tenant_payment_record = TenantPaymentRecord
