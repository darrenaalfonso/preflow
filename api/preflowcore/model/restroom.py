from ..model.location import Location
from django.db import models

SEX_CHOICES = [(1, 'Male'), (2, 'Female'), (3, 'No Distinction'), (4, 'Other')]
TOWEL_DISPENSER_TYPE_CHOICES = [(1, 'Manual'), (2, 'Automatic'), (3, 'Other'), (4, 'None')]
HAND_DRYER_TYPE_CHOICES = [(1, 'Button'), (2, 'Sensor'), (3, 'None'), (4, 'Other')]
HAND_SOAP_DISPENSER_TYPE_CHOICES = [(1, 'Automatic'), (2, 'Manual'), (3, 'Bar'), (4, 'None'), (5, 'Other')]
FLUSH_TYPE_CHOICES = [(1, 'Automatic'), (2, 'Manual'), (3, 'Water Saving'), (4, 'None'), (5, 'Other')]
TOILET_PAPER_DISPENSER_TYPE_CHOICES = [(1, 'Perpendicular'), (2, 'Parallel'), (3, 'Other')]


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
