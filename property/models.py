from django.db import models

from app_users.models import (
    user_detail_class,
    location_class,
    company_management_class,
    tenant_details_class,
    tenants_record_class,
    tenant_payment_record,
)

# class MyManager ( models.Manager ):
#
#   def filter_by_instance(self, instance):
#       content_type = ContentType.objects.get_for_model(instance.__class__)
#       obj_id = instance.id
#       qs = super(MyManager, self).filter(content_type=content_type, object_id= obj_id)
#       return qs

class PropertyDetail (models.Model):
    TYPE_OPTIONS = (
        ('Apartments','Apartments'),
        ('Houses','Houses'),
        ('Offices-Bussiness units','Offices-Bussiness units'),
    )

    location = models.ForeignKey(location_class, on_delete=models.SET_NULL, null=True)
    property_name = models.CharField (max_length = 50,null=True)
    property_type = models.CharField (max_length = 50,null=True, choices=TYPE_OPTIONS)
    number_of_units = models.IntegerField (null=True)
    availlable_units = models.IntegerField (null=True)
    occupied_units = models.IntegerField (null=True)
    property_overview_photo = models.FileField (null=True)
    administrator = models.ForeignKey (user_detail_class, on_delete=models.SET_NULL, null=True)
    management_company = models.ForeignKey(company_management_class, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "%s" %(self.property_name)

class UnitDetail (models.Model):
    propertyDetail = models.ForeignKey (PropertyDetail,on_delete = models.CASCADE,null=True)
    unit_ID = models.CharField (max_length = 10,null=True)
    unit_size = models.CharField (max_length = 50,null=True)
    number_of_rooms = models.CharField (max_length = 10,null=True)
    unit_value = models.IntegerField(blank = True, null = True)
    unit_purpose = models.CharField (max_length = 20,null=True)
    tenant_details = models.ForeignKey (tenant_details_class, on_delete=models.SET_NULL, null=True)
    tenant_records = models.ForeignKey (tenants_record_class, on_delete=models.SET_NULL, null=True)
    tenant_current_month_payment_status = models.ForeignKey(tenant_payment_record, on_delete=models.SET_NULL, null=True)

class UnitPictures (models.Model):
    unit_ID = models.ForeignKey(UnitDetail, on_delete = models.CASCADE,null = True, blank = True)
    pictures = models.FileField(null = True, blank = True)


property_class = PropertyDetail
unitdetail_class = UnitDetail
UnitPictures_class = UnitPictures
