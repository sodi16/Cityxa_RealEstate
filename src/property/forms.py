from django import forms
from django.contrib.auth import get_user_model

from property.models import Property, ImageDescription
from users.models import Adress
from django.forms import TextInput, ClearableFileInput


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = ImageDescription
        fields = ['image']
        widgets = {
            'image': ClearableFileInput(attrs={'multiple': True}),
        }


class AddAdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['country', 'city', 'street', 'num_apt', 'zip_code', 'longitude', 'latitude']


class AddPropertyForm(forms.ModelForm):
    adress_form = AddAdressForm()
    min_price = forms.IntegerField(min_value=1, required=False)
    max_price = forms.IntegerField(max_value=9999999, required=False)

    min_num_rooms = forms.IntegerField(min_value=1, required=False)
    max_num_rooms = forms.IntegerField(max_value=20, required=False)

    class Meta:
        model = Property
        exclude = ['owner', 'posted_date', 'adress', 'clicked_time', 'images', 'longitude', 'latitude']

        widgets = {
            'furniture': forms.CheckboxInput(),
            'build_year': forms.DateTimeField(),
            'elevator': forms.CheckboxInput(),
            'balcony': forms.CheckboxInput(),
            'swimming_pool': forms.CheckboxInput(),
            'renovated': forms.CheckboxInput(),
            'storage': forms.CheckboxInput(),
            'disable_access': forms.CheckboxInput(),
            'safe_room': forms.CheckboxInput(),
            'central_air_conditioner': forms.CheckboxInput(),
            'quiet_neighborhood': forms.CheckboxInput(),
        }

        labels = {
            'id_type_of_property': 'Property type',
            'id_rent_buy': 'Rent/Buy',
            'min_price': 'Min price',
            'max_price': 'Max price',
            'min_num_rooms': 'Min bedrooms',
            'max_num_rooms': 'Max bedrooms'
        }
