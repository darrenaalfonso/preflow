from ..model import Location
from django.contrib.auth.models import User
from ..serializer.location_serializer import LocationSerializer
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse


class LocationViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

    def perform_create(self, serializer):
        serializer.save()
