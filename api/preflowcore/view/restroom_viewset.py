from ..model import Restroom
from ..serializer.restroom_serializer import RestroomSerializer
from rest_framework import viewsets


class RestroomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update' and 'destroy' actions.
    """
    queryset = Restroom.objects.all()
    serializer_class = RestroomSerializer
