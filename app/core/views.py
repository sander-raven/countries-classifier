import django_tables2 as tables

from core.models import Country
from core.tables import CountryTable


class CountryTableView(tables.SingleTableView):
    table_class = CountryTable
    queryset = Country.objects.all()
    paginate_by = 15
    template_name = 'country_list.html'
