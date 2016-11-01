from ..model import Location
from rest_framework import serializers


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ('url', 'pk', 'name', 'street_number', 'street_name', 'unit_number', 'city', 'state', 'zip_code')
