from rest_framework import serializers
from ..model.location import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Location
        fields = ('url', 'pk', 'name', 'street_number', 'street_name', 'unit_number', 'city', 'state', 'zip')
