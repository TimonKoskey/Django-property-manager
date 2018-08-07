from property_management.models import (
    property_class,
    unitdetail_class,
    )

from userAuthentication.serializers.serializers import (
    TenantsListSerializer,
    UserSerializer,
    LocationSerializer,
    AgencyDetailsSerializer
    )

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from rest_framework.serializers import (
	EmailField,
	CharField,
	ModelSerializer,
	HyperlinkedIdentityField,
	SerializerMethodField,
	)

user=get_user_model()

class PropertiesListSerializer ( ModelSerializer ):
    Administrator = SerializerMethodField()
    Location = SerializerMethodField()
    Agency = SerializerMethodField()
    class Meta:
        model = property_class
        fields = [
            'id',
            'Property_overview_photo',
            'Property_name',
            'Location',
            'Agency',
            'Administrator'
        ]
    def get_Administrator (self,obj):
        Administrator = UserSerializer (obj.Administrator.User_details).data
        return Administrator

    def get_Location (self,obj):
        Location = LocationSerializer (obj.Location).data
        return Location

    def get_Agency (self,obj):
        Agency = AgencyDetailsSerializer (obj.Agency).data
        return Agency

class PropertyDetailsSerializer ( ModelSerializer ):
    units_list = SerializerMethodField()
    Administrator = SerializerMethodField()
    Location = SerializerMethodField()

    class Meta:
        model = property_class
        fields = [
            'Property_overview_photo',
            'Property_name',
            'Property_type',
            'Location',
            'Number_of_units',
            'Availlable_units',
            'Administrator',
            'Occupied_units',
            'units_list'
        ]

    def get_units_list ( self,obj):
        units_list_qs = objects = unitdetail_class.objects.filter_by_instance(obj)
        units_list = UnitsListSerializer (units_list_qs,many = True).data
        return units_list

    def get_Administrator (self,obj):
        Administrator = UserSerializer (obj.Administrator.User_details).data
        return Administrator

    def get_Location (self,obj):
        Location = LocationSerializer (obj.Location).data
        return Location

class UnitsListSerializer ( ModelSerializer ):
    tenant = SerializerMethodField()
    class Meta:
        model = unitdetail_class
        fields = [
            'Unit_ID',
            'Unit_size',
            'Number_of_rooms'
            'tenant'
        ]
    def get_tenant(self,obj):
        tenant = TenantsListSerializer(obj.Tenant_ID).data
        return tenant
