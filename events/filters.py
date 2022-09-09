# developers/view.py
from django_filters import rest_framework as filters

from events.models import Event
from events.serializers import EventDistanceSerializer

...


class DistanceFilter(filters.FilterSet):
    dist_gte = filters.NumberFilter(field_name="duration", lookup_expr="gte")
    dist_lte = filters.NumberFilter(field_name="duration", lookup_expr="lte")

    class Meta:
        model = Event
        fields = []
