import django_tables2 as tables

from core.models import Country


class CountryTable(tables.Table):
    flag = tables.TemplateColumn(
        '''{% load static %}<img src="{% static'''
        ''' 'core/flags/32x24/'|add:record.alpha2_code.lower'''
        '''|add:'.png' %}" alt="{{ record.alpha2_code }}" />''',
        orderable=False,
        verbose_name='Флаг',
    )

    class Meta:
        model = Country
        template_name = 'django_tables2/bootstrap5-responsive.html'
        fields = (
            'numeric_code',
            'flag',
            'short_name',
            'full_name',
            'alpha2_code',
            'alpha3_code',
            'region',
        )
