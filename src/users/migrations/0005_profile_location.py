# Generated by Django 5.0.6 on 2024-05-27 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_location_state_location_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.location'),
        ),
    ]
