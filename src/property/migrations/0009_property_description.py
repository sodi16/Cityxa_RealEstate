# Generated by Django 4.1.7 on 2023-03-07 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_remove_property_latitude_remove_property_longitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
