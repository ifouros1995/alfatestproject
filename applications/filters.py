import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import DateInput

from .models import *

class OrderFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date", lookup_expr='gte')
	# end_date = DateFilter(field_name="date", lookup_expr='lte')
	# note = CharFilter(field_name='note', lookup_expr='icontains')
	name = CharFilter(field_name='name', lookup_expr='icontains')
	date = DateFilter(
        widget=DateInput(
            attrs={
                'type': 'date'
            }
        )
    )



	class Meta:
		model = Application
		fields = '__all__'
		exclude = ['address', 'status_list', 'protocol_number']
