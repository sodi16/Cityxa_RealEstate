# Generated by Django 4.1.7 on 2023-03-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_properties'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profil_picture',
            field=models.ImageField(default='profil_pictures/default_profile_picture.jpg', upload_to='profil_pictures', verbose_name='property.ImageDescription'),
        ),
    ]