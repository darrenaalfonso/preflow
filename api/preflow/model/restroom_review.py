from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .location import Location
from .restroom import Restroom
from django.contrib.auth.models import User


class RestroomReview(models.Model):
    pid = models.CharField(max_length=10, db_index=True)
    owner = models.ForeignKey(User, related_name='restroom_reviews')
    location = models.ForeignKey(Location, related_name='restroom_reviews')
    restroom = models.ForeignKey(Restroom, related_name='restroom_reviews')
    comment = models.TextField
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    row_stamp = models.DateTimeField(auto_now_add=True)
