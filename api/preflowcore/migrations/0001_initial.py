# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-23 05:04
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(db_index=True, max_length=10)),
                ('latitude', models.TextField(db_index=True)),
                ('longitude', models.TextField(db_index=True)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('street_number', models.CharField(max_length=10)),
                ('street_name', models.TextField(db_index=True)),
                ('unit_number', models.CharField(max_length=10)),
                ('city', models.CharField(db_index=True, max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=2)),
                ('zip_code', models.CharField(db_index=True, max_length=10)),
                ('row_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(db_index=True, max_length=10)),
                ('latitude', models.TextField(db_index=True)),
                ('longitude', models.TextField(db_index=True)),
                ('sex', models.CharField(choices=[(1, 'Male'), (2, 'Female'), (3, 'No Distinction'), (4, 'Other')], max_length=100)),
                ('towel_dispenser_type', models.CharField(choices=[(1, 'Manual'), (2, 'Automatic'), (3, 'Other'), (4, 'None')], max_length=100)),
                ('hand_dryer_type', models.CharField(choices=[(1, 'Button'), (2, 'Sensor'), (3, 'None'), (4, 'Other')], max_length=100)),
                ('hand_soap_dispenser_type', models.CharField(choices=[(1, 'Automatic'), (2, 'Manual'), (3, 'Bar'), (4, 'None'), (5, 'Other')], max_length=100)),
                ('flush_type', models.CharField(choices=[(1, 'Automatic'), (2, 'Manual'), (3, 'Water Saving'), (4, 'None'), (5, 'Other')], max_length=100)),
                ('toilet_paper_dispenser_type', models.CharField(choices=[(1, 'Perpendicular'), (2, 'Parallel'), (3, 'Other')], max_length=100)),
                ('row_stamp', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restrooms', to='preflowcore.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RestroomReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(db_index=True, max_length=10)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('row_stamp', models.DateTimeField(auto_now_add=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restroom_reviews', to='preflowcore.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restroom_reviews', to=settings.AUTH_USER_MODEL)),
                ('restroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restroom_reviews', to='preflowcore.Restroom')),
            ],
        ),
    ]