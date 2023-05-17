import django_filters
from django.db.models import Q

from core.models import Country


class CountryFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(
        method='search',
        label='Поиск',
    )

    class Meta:
        model = Country
        fields = ['query']

    def search(self, queryset, name, value):
        filtered_queryset = queryset.filter(
            Q(short_name__icontains=value) |
            Q(full_name__icontains=value) |
            Q(numeric_code__icontains=value) |
            Q(alpha2_code__icontains=value) |
            Q(alpha3_code__icontains=value) |
            Q(region__name__icontains=value)
        )
        return filtered_queryset
