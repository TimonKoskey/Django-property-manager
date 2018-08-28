from django.contrib import admin
from .models import (
    property_class,
    unitdetail_class,
    )

class UnitsInline (admin.TabularInline):
    model = unitdetail_class

class PropertyAdmin (admin.ModelAdmin):

    inlines = [ UnitsInline ]

    def get_formsets_with_inlines(self,request,obj=None):
        for inline in self.get_inline_instances(request,obj):
            yield inline.get_formset(request,obj),inline

admin.site.register(property_class,PropertyAdmin)
# admin.site.register(unitdetail_class)
