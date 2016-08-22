from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'reviews')
