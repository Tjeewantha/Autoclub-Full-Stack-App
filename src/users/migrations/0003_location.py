# Generated by Django 5.0.6 on 2024-05-26 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_image_profile_photo_profile_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(blank=True, max_length=128)),
                ('city', models.CharField(max_length=64)),
            ],
        ),
    ]
