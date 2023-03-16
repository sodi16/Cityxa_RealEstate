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

    class Meta:
        model = Property
        exclude = ['owner', 'posted_date', 'adress', 'clicked_time', 'images', 'longitude', 'latitude']

        widgets = {
            'furniture': forms.CheckboxInput(),
            'build_year': forms.CheckboxInput(),
            'elevator': forms.CheckboxInput(),
            'balcony': forms.CheckboxInput(),
            'swimming_pool': forms.CheckboxInput(),
            'renovated': forms.CheckboxInput(),
            'storage': forms.CheckboxInput(),
            'disable_access': forms.CheckboxInput(),
            'safe_room': forms.CheckboxInput(),
            'central_air_conditioner': forms.CheckboxInput(),
            'quiet_neighborhood': forms.CheckboxInput(),

            'id_type_of_property': forms.CheckboxSelectMultiple(),
            'num_rooms': forms.CheckboxSelectMultiple(),
        }

