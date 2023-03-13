from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cityxa import settings


def get_property_model():
    """
    Solution for circular import
    """
    from django.apps import apps
    Adress = apps.get_model('users.Adress')
    return Adress



class ImageDescription(models.Model):
    image = models.ImageField(upload_to='property_photos', default=f'property_photos/home_default.png')
    default_shape = (640, 480)

    # def save(self, *args, **kwargs):
    #     super(ImageDescription, self).save()


class Property(models.Model):
    rent_buy_choices = (
        (1, 'Rent'),
        (2, 'Buy')
    )
    type_of_property = (
        (1, 'appartment'),
        (2, 'villa'),
        (3, 'duplex'),
        (4, 'floor-appartment'),
        (5, 'vacation Apartment'),
        (6, 'basement floor'),
        (7, 'studio/loft'),
        (8, 'roof/penthouse'),
        (9, 'office'),
    )

    owner = models.ForeignKey(get_user_model(), on_delete=models.CharField, default=get_user_model())
    id_rent_buy = models.PositiveSmallIntegerField(choices=rent_buy_choices, default=1)
    id_type_of_property = models.PositiveSmallIntegerField(choices=type_of_property, default=1)
    adress = models.OneToOneField('users.Adress', on_delete=models.CASCADE)
    price = models.IntegerField()
    num_rooms = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(20)])
    description = models.TextField(max_length=1500, blank=True)
    area = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    furniture = models.BooleanField(blank=True, null=True)
    elevator = models.BooleanField(blank=True, null=True)
    swimming_pool = models.BooleanField(blank=True, null=True)
    balcony = models.BooleanField(blank=True, null=True)
    renovated = models.BooleanField(blank=True, null=True)
    storage = models.BooleanField(blank=True, null=True)
    disable_access = models.BooleanField(blank=True, null=True)
    safe_room = models.BooleanField(blank=True, null=True)
    central_air_conditioner = models.BooleanField(blank=True, null=True)
    quiet_neighborhood = models.BooleanField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now=True)
    images = models.ManyToManyField(ImageDescription, default='property_photos/home_default.png')
    clicked_time = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.num_rooms} bedrooms in {self.adress.city}, {self.adress.country}'

    def display_rent_buy(self):
        return str(self.rent_buy_choices[int(self.id_rent_buy)-1][1])

    def display_type_of_property(self):
        return str(self.type_of_property[int(self.id_type_of_property)-1][1]).capitalize()

