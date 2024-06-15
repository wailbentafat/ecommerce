import django_filters
from .models import product
class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword=django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    minprice = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    maxprice = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = product
        fields = ['brand', 'name', 'price']