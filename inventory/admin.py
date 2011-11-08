from inventory.models import *
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class ObjectsAdmin(admin.ModelAdmin):
    list_display = ('common_name', 'product_name', 'manufacturer', 'location',
    'reference_person', 'out_of_accreditation')
    list_filter = ( 'out_of_accreditation', 'reference_person' )
    fieldsets = [
        (None,  {'fields': ['common_name', 'product_name', 'manufacturer',
        'standard_apparal', 'out_of_accreditation', 'reference_person']}),
        (_('Product information'), {'fields': ['product_type',
            'serial_number']}),
        (_('Description'), {'fields': ['tech_specs', 'env_cond',
            'precautions']}),
        (_('Position'), {'fields': ['location', 'user_guide_location']}),
        (_('Maintenance'), {'fields': ['maintenance_days', 'maintenance_text',
            'maintenance_date', 'next_maintenance_date', 'control_days',
            'control_text', 'control_date', 'next_control_date',
            'calibration_days', 'calibration_text', 'calibration_date',
            'next_calibration_date', 'overlap_days'], 'classes': ['collapse']}),
        (_('Assets'), {'fields': ['assets'], 'classes': ['collapse']}),
        (_('Purchase'), {'fields': ['purchase_date', 'bought_new', 'price',
            'order_date', 'activation_date', 'guarantee', 'end_date',
            'end_reason'], 'classes': ['collapse']}),
        (_('Instructions'), {'fields': ['usage_reference', 'usage',
            'maintenance_reference', 'maintenance', 'calibration_reference',
            'calibration', 'control_reference', 'control'], 'classes':
            ['collapse']}),

    ]

class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'zip_code', 'country')
    list_filter = ['country']

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city')

class SiteAdmin(admin.ModelAdmin):
    list_display = ('city', 'address')

admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Object, ObjectsAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Site, SiteAdmin)
