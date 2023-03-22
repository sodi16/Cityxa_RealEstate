from django.contrib.auth.models import AbstractUser
from django.db import models


class Adress(models.Model):
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=100, null=True, blank=True)
    num_apt = models.IntegerField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.street}, {self.city} {self.country}'


class Role(models.Model):
    ROLE_CHOICES = (
        (1, 'Customer'),
        (2, 'Renter/Seller'),
        (3, 'RealEstateAgent'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.ROLE_CHOICES[self.id - 1][1]


class User(AbstractUser):
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=12)
    creation_date = models.DateTimeField(auto_now_add=True)
    role = models.ManyToManyField(Role, default=1)
    birthdate = models.DateField(null=True, blank=True)
    properties = models.ManyToManyField('property.Property', blank=True)
    profil_picture = models.ImageField('property.ImageDescription', upload_to='profil_pictures', default=f'profil_pictures/default_profile_picture.jpg')

    # add fields when creating super user
    REQUIRED_FIELDS = ['phone_number']

    def display_role(self):
        res = ''
        for role in self.role:
            res += role
        return res

