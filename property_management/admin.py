from django.contrib import admin
from .models import (
    property_class,
    unitdetail_class,
    )

admin.site.register(property_class)
admin.site.register(unitdetail_class)
