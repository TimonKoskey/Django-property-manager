from django.db import models
from userAuthentication.models import classNames,tenant_class

class MyManager ( models.Manager ):

  def filter_by_instance(self, instance):
    qs = super(MyManager, self).filter( Property_ID = instance )
    return qs

class PropertyDetail (models.Model):
    Property_name = models.CharField (max_length = 50,null=True)
    Property_type = models.CharField (max_length = 50,null=True)
    Location = models.ForeignKey (classNames['LocationClass'],on_delete = models.CASCADE,null=True)
    Number_of_units = models.IntegerField (null=True)
    Availlable_units = models.IntegerField (null=True)
    Occupied_units = models.IntegerField (null=True)
    Property_overview_photo = models.FileField (null=True)
    Agency = models.ForeignKey (classNames['AgencyClass'],on_delete = models.CASCADE,null=True)
    Administrator = models.ForeignKey (classNames['AdministratorClass'],on_delete = models.CASCADE,
                                        blank = True,
                                        null=True)

    def __str__(self):
        return "%s" %(self.Property_name)

class UnitDetail (models.Model):
    Property_ID = models.ForeignKey (PropertyDetail,on_delete = models.CASCADE,null=True)
    Unit_ID = models.CharField (max_length = 10,null=True)
    Unit_size = models.CharField (max_length = 10,null=True)
    Number_of_rooms = models.CharField (max_length = 10,null=True)
    Is_occupied = models.BooleanField (default = False)
    Tenant_ID = models.ForeignKey (tenant_class,on_delete = models.CASCADE,null=True)

    objects = MyManager()

property_class = PropertyDetail
unitdetail_class = UnitDetail
