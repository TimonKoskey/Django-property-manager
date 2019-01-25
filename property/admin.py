from django.contrib import admin
from .models import (
    property_class,
    unitdetail_class,
    UnitPictures_class,
)

class PhotosInline (admin.TabularInline):
    model = UnitPictures_class

class UnitAdmin (admin.ModelAdmin):

    inlines = [ PhotosInline ]

    def get_formsets_with_inlines(self,request,obj=None):
        for inline in self.get_inline_instances(request,obj):
            yield inline.get_formset(request,obj),inline

admin.site.register(property_class)
admin.site.register(unitdetail_class, UnitAdmin)
