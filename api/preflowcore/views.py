from django.shortcuts import render
from .serializer.location_serializer import LocationSerializer
from .serializer.restroom_serializer import RestroomSerializer
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format)
    })


