from ..model.location import Location
from ..model.restroom import Restroom
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class RestroomReview(models.Model):
    pid = models.CharField(max_length=10, db_index=True)
    owner = models.ForeignKey(User, related_name='restroom_reviews')
    location = models.ForeignKey(Location, related_name='restroom_reviews')
    restroom = models.ForeignKey(Restroom, related_name='restroom_reviews')
    comment = models.TextField
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    row_stamp = models.DateTimeField(auto_now_add=True)
