# Generated by Django 3.1.7 on 2023-02-20 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='adress',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]