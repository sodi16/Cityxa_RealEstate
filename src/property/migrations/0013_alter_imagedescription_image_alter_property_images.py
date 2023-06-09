# Generated by Django 4.1.7 on 2023-03-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_alter_imagedescription_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedescription',
            name='image',
            field=models.ImageField(default='home_default.png', upload_to='property_photos'),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.ManyToManyField(to='property.imagedescription'),
        ),
    ]
