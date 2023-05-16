from django.contrib import admin
from import_export import fields, resources
from import_export.admin import ImportExportMixin
from import_export.widgets import ForeignKeyWidget

from core.models import Region


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
