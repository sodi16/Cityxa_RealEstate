# Generated by Django 4.1.7 on 2023-03-13 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_alter_imagedescription_image_alter_property_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagedescription',
            name='image',
            field=models.ImageField(default='property_photos/home_default.png', upload_to='property_photos'),
        ),
        migrations.AlterField(
            model_name='property',
            name='images',
            field=models.ManyToManyField(default='property_photos/home_default.png', to='property.imagedescription'),
        ),
    ]
