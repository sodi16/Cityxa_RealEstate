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

        # widgets = {
        #     'furniture': forms.HiddenInput(),
        #     'build_year': forms.HiddenInput(),
        #     'elevator': forms.HiddenInput(),
        #     'balcony': forms.HiddenInput(),
        #     'swimming_pool': forms.HiddenInput(),
        #     'renovated': forms.HiddenInput(),
        #     'storage': forms.HiddenInput(),
        #     'disable_access': forms.HiddenInput(),
        #     'safe_room': forms.HiddenInput(),
        #     'central_air_conditioner': forms.HiddenInput(),
        #     'quiet_neighborhood': forms.HiddenInput()
        # }

