from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .view import location_viewset, restroom_viewset


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'locations', location_viewset.LocationViewSet)
router.register(r'restrooms', restroom_viewset.RestroomViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
