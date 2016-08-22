from django.db import models
from .location import Location


SEX_CHOICES = ['male', 'female', 'none', 'other']
TOWEL_DISPENSER_TYPE_CHOICES = ['lever', 'automatic', 'pull', 'other', 'none']
HAND_DRYER_TYPE_CHOICES = ['button', 'automatic', 'none', 'other']
HAND_SOAP_DISPENSER_TYPE_CHOICES = ['automatic', 'bar', 'pump', 'none', 'other']
FLUSH_TYPE_CHOICES = ['automatic', 'manual', 'dual', 'none', 'other']
TOILET_PAPER_DISPENSER_TYPE_CHOICES = ['perpendicular', 'parallel', 'other']


class Restroom(models.Model):
    pid = models.CharField(max_length=10, db_index=True)
    latitude = models.TextField(db_index=True)
    longitude = models.TextField(db_index=True)
    location = models.ForeignKey(Location, related_name='restrooms')
    floor = models.IntegerField
    is_single_occupancy = models.BooleanField
    stalls = models.IntegerField
    sex = models.CharField(choices=SEX_CHOICES, max_length=100)
    towel_dispenser_type = models.CharField(choices=TOWEL_DISPENSER_TYPE_CHOICES, max_length=100)
    hand_dryer_type = models.CharField(choices=HAND_DRYER_TYPE_CHOICES, max_length=100)
    hand_soap_dispenser_type = models.CharField(choices=HAND_SOAP_DISPENSER_TYPE_CHOICES, max_length=100)
    flush_type = models.CharField(choices=FLUSH_TYPE_CHOICES, max_length=100)
    toilet_paper_dispenser_type = models.CharField(choices=TOILET_PAPER_DISPENSER_TYPE_CHOICES, max_length=100)
    toilet_seat_covers = models.BooleanField
    row_stamp = models.DateField(auto_now_add=True)

