from ..model import Restroom
from rest_framework import serializers


class RestroomSerializer(serializers.HyperlinkedModelSerializer):
    location = serializers.HyperlinkedIdentityField(view_name='location-viewset', source='location.pid')
    # reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True)

    class Meta:
        model = Restroom
        fields = ('url', 'pk', 'location', 'floor', 'is_single_occupancy', 'stalls', 'sex', 'towel_dispenser_type',
                  'hand_dryer_type', 'hand_soap_dispenser_type', 'flush_type', 'toilet_paper_dispenser_type',
                  'toilet_seat_covers')
