# Generated by Django 3.1.7 on 2023-02-23 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_city_street'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='floor',
        ),
    ]
