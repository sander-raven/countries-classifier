from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from core.filters import CountryFilter
from core.models import Country
from core.tables import CountryTable


class CountryTableView(SingleTableMixin, FilterView):
    table_class = CountryTable
    model = Country
    filterset_class = CountryFilter
    paginate_by = 15
    template_name = 'core/country_list.html'
