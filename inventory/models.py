from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(_('name'), max_length=16)

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')

    def __unicode__(self):
        return self.name

class City(models.Model):
    name = models.CharField(_('name'), max_length=32)
    zip_code = models.IntegerField(_('zip code'))
    country = models.ForeignKey(Country, verbose_name=_('country'))

    class Meta:
        verbose_name = _('city')
        verbose_name_plural = _('cities')

    def __unicode__(self):
        return self.name

class Site(models.Model):
    city = models.ForeignKey(City, verbose_name=_('city'))
    address = models.CharField(_('address'), max_length=64)

    class Meta:
        verbose_name = _('site')
        verbose_name_plural = _('sites')

    def __unicode__(self):
        return self.city.__unicode__()

class Location(models.Model):
    site = models.ForeignKey(Site, verbose_name=_('site'))
    room = models.CharField(_('room'), max_length=32)

    class Meta:
        verbose_name = _('position')
        verbose_name_plural = _('positions')

    def __unicode__(self):
        return self.room + ' - ' + self.site.__unicode__()

class Manufacturer(models.Model):
    company_name = models.CharField(_('company name'), max_length=32)
    city = models.ForeignKey(City, verbose_name=_('city'))
    address = models.CharField(_('address'), max_length=64, blank=True)
    phone_number = models.CharField(_('phone number'), max_length=16,
        blank=True)
    fax_number = models.CharField(_('fax number'), max_length=16, blank=True)
    contact_name = models.CharField(_('contact name'), max_length=32,
        blank=True)
    contact_phone_number = models.CharField(_('contact phone number'),
        max_length=32, blank=True)

    class Meta:
        verbose_name = _('manufacturer')
        verbose_name_plural = _('manufacturers')

    def __unicode__(self):
        return self.company_name

class Object(models.Model):
    common_name = models.CharField(_('common name'), max_length=64)
    product_name = models.CharField(_('product name'), max_length=64)

    product_type = models.CharField(_('product type'), max_length=32,
        blank=True, null=True)
    serial_number = models.CharField(_('serial number'), max_length=32,
        blank=True, null=True)

    standard_apparal = models.BooleanField(_('standard apparal'))

    location = models.ForeignKey(Location, blank=True, null=True,
        verbose_name=_('position'))
    user_guide_location = models.ForeignKey(Location,
        related_name='user_guide_location', blank=True, null=True,
        verbose_name=_('user guide location'))
    manufacturer = models.ForeignKey(Manufacturer,
        verbose_name=_('manufacturer'), blank=True, null=True)
    reference_person = models.ForeignKey(User,
        verbose_name=_('reference person'), blank=True, null=True)

    tech_specs = models.TextField(_('technical specifications'), blank=True,
        null=True)
    precautions = models.TextField(_('precautions'), blank=True,
        null=True)
    env_cond = models.TextField(_('environnemental specification'), blank=True,
        null=True)

    assets = models.TextField(_('assets'), blank=True, null=True)

    out_of_accreditation = models.BooleanField(_('out of accreditation'))

    start_date = models.DateField(_('start date'), blank=True, null=True)
    end_date = models.DateField(_('end date'), blank=True, null=True)
    end_reason = models.CharField(_('end reason'), max_length=64, blank=True,
        null=True)

    control_text = models.CharField(_('control'), max_length=64, blank=True,
        null=True)
    maintenance_text = models.CharField(_('maintenace'), max_length=64,
        blank=True, null=True)
    calibration_text = models.CharField(_('calibration'), max_length=64,
        blank=True, null=True)
    calibration_days = models.IntegerField(_('calibration frequency'),
        blank=True, null=True)
    maintenance_days = models.IntegerField(_('maintenance frequency'),
        blank=True, null=True)
    control_days = models.IntegerField(_('control frequeency'), blank=True,
        null=True)
    overlap_days = models.IntegerField(_('overlap days'), blank=True,
        null=True)
    calibration_date = models.DateField(_('calibration date'), blank=True,
        null=True)
    control_date = models.DateField(_('control date'), blank=True, null=True)
    maintenance_date = models.DateField(_('maintenance date'), blank=True,
        null=True)
    last_maintenance_date = models.DateField(_('last maintenance date'),
        blank=True, null=True)
    last_calibration_date = models.DateField(_('last calibration date'),
        blank=True, null=True)
    last_control_date = models.DateField(_('last control date'), blank=True,
        null=True)

    purchase_date = models.DateField(_('purchase date'), blank=True, null=True)
    bought_new = models.BooleanField(_('bought new'))
    price = models.IntegerField(_('price'), blank=True, null=True)
    order_date = models.DateField(_('order date'), blank=True, null=True)
    activation_date = models.DateField(_('activation date'), blank=True,
        null=True)
    guarantee = models.DateField(_('guarantee date'), blank=True,
        null=True)

    usage = models.TextField(_('usage'), blank=True, null=True)
    maintenance = models.TextField(_('maintenance'),
        blank=True, null=True)
    calibration = models.TextField(_('calibration'),
        blank=True, null=True)
    control = models.TextField(_('control'), blank=True, null=True)
    usage_reference = models.CharField(_('usage'), max_length=64, blank=True,
        null=True)
    maintenance_reference = models.CharField(_('maintenance'), max_length=64,
        blank=True, null=True)
    calibration_reference = models.CharField(_('calibration'), max_length=64,
        blank=True, null=True)
    control_reference = models.CharField(_('control'), max_length=64,
        blank=True, null=True)

    class Meta:
        verbose_name = _('object')
        verbose_name_plural = _('objects')

    def __unicode__(self):
        return self.common_name

