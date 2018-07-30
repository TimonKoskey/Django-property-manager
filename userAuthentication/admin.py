from django.contrib import admin
from .models import (
    agency_class,
    superadmin_class,
    admin_class,
    tenant_class,
    location_class,
    avatar_class
)

admin.site.register( agency_class )
admin.site.register( superadmin_class )
admin.site.register( admin_class )
admin.site.register( tenant_class )
admin.site.register( location_class )
admin.site.register( avatar_class )
