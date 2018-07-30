from userAuthentication.models import (
    agency_class,
    superadmin_class,
    admin_class,
    tenant_class,
    location_class,
    avatar_class
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

class TenantsListSerializer ( ModelSerializer ):
    name = SerializerMethodField()

    class Meta:
        model = tenant_class
        fields = [
            'name',
            'Entry_date'
        ]
    def get_name(self,obj):
        name = UserSerializer(obj.User_details).data
        return name

class UserSerializer ( ModelSerializer ):
    class Meta:
        model = user
        fields = [
            'username', 
            'first_name',
            'last_name'
        ]

class LocationSerializer ( ModelSerializer ):

    class Meta:
        model = location_class
        fields = [
            'County',
            'City_or_Town',
            'Area_name'
        ]

class AgencyDetailsSerializer ( ModelSerializer ):
    Office_location = SerializerMethodField()

    class Meta:
        model = agency_class
        fields = [
            'Agency_name',
            'Phone_number',
            'Email_address',
            'Website',
            'Office_location'
        ]

    def get_Office_location (self,obj):
        Office_location = LocationSerializer (obj.Office_location).data
        return Office_location

class AgencyAdminDetailsSerializer ( ModelSerializer ):
    User_details = SerializerMethodField()
    Agency_details = SerializerMethodField()

    class Meta:
        model = admin_class
        fields = [
            'User_details',
            'Agency_details'
        ]

    def get_User_details (self,obj):
        User_details = UserSerializer(obj.User_details).data
        return User_details

    def get_Agency_details (self,obj):
        Agency_details = AgencyDetailsSerializer(obj.Agency_details).data
        return Agency_details

class AgencySuperAdminDetailsSerializer ( ModelSerializer ):
    User_details = SerializerMethodField()
    Agency_details = SerializerMethodField()

    class Meta:
        model = superadmin_class
        fields = [
            'User_details',
            'Agency_details'
        ]

    def get_User_details (self,obj):
        User_details = UserSerializer(obj.User_details).data
        return User_details

    def get_Agency_details (self,obj):
        Agency_details = AgencyDetailsSerializer(obj.Agency_details).data
        return Agency_details
