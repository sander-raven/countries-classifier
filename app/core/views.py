from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from core.filters import CountryFilter
from core.models import Country
from core.tables import CountryTable


class CountryTableView(SingleTableMixin, FilterView):
    table_class = CountryTable
    model = Country
    filterset_class = CountryFilter
    paginate_by = 10
    # template_name = 'core/country_list.html'

    def get_template_names(self):
        if self.request.htmx:
            template_name = 'core/country_list_partial.html'
        else:
            template_name = 'core/country_list.html'
        return template_name
