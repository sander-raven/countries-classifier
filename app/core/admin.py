from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

from core.models import Region, Country


class RegionResource(resources.ModelResource):
    parent = fields.Field(
        column_name='parent',
        attribute='parent',
        widget=ForeignKeyWidget(Region, field='name'),
    )

    def before_import_row(self, row, **kwargs):
        parent_name = row['parent']
        if parent_name:
            Region.objects.get_or_create(
                name=parent_name, defaults={'name': parent_name}
            )

    class Meta:
        model = Region
        fields = ('name', 'parent', 'order', 'id')


class CountryResource(resources.ModelResource):
    region = fields.Field(
        column_name='region',
        attribute='region',
        widget=ForeignKeyWidget(Region, field='name'),
    )

    def before_import_row(self, row, **kwargs):
        region_name = row['region']
        if region_name:
            Region.objects.get_or_create(
                name=region_name, defaults={'name': region_name}
            )

    class Meta:
        model = Country
        fields = (
            'id',
            'numeric_code',
            'short_name',
            'full_name',
            'alpha2_code',
            'alpha3_code',
            'region',
        )


@admin.register(Region)
class RegionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'parent', 'order')
    list_display_links = ('name', )
    search_fields = ('name', )
    list_filter = ('parent', )
    fields = ('id', 'name', 'parent', 'order')
    readonly_fields = ('id', )
    ordering = ('order', 'name')
    resource_class = RegionResource


@admin.register(Country)
class CountryAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = (
        'numeric_code',
        'short_name',
        'full_name',
        'alpha2_code',
        'alpha3_code',
        'region',
    )
    list_display_links = ('short_name', 'full_name')
    search_fields = (
        'numeric_code',
        'short_name',
        'full_name',
        'alpha2_code',
        'alpha3_code',
        'region__name',
    )
    list_filter = ('region', )
    fields = (
        'id',
        'numeric_code',
        'short_name',
        'full_name',
        'alpha2_code',
        'alpha3_code',
        'region',
    )
    readonly_fields = ('id', )
    ordering = (
        'numeric_code',
        'short_name',
        'alpha2_code',
        'alpha3_code',
    )
    resource_class = CountryResource
