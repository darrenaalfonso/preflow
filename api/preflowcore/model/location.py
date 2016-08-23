from django.db import models


class Location(models.Model):
    pid = models.CharField(max_length=10, db_index=True)
    latitude = models.TextField(db_index=True)
    longitude = models.TextField(db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    street_number = models.CharField(max_length=10)
    street_name = models.TextField(db_index=True)
    unit_number = models.CharField(max_length=10)
    city = models.CharField(max_length=20, db_index=True)
    state = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10, db_index=True)
    row_stamp = models.DateTimeField(auto_now_add=True)
