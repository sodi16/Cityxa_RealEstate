from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django import forms
from django.core.exceptions import ValidationError

from property.models import Property
from users.models import Adress
from django.forms.widgets import NumberInput, TextInput


class AdressForm(forms.ModelForm):
    class Meta:
        model = Adress
        fields = ['country', 'city', 'street', 'num_apt', 'zip_code']


class LoginForm(LoginView):
    template_name = 'base/login.html'


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        template_name = 'base/register.html'
        fields = ('username', 'first_name', 'last_name', 'adress', 'birthdate', 'phone_number')
        widgets = {'birthdate': forms.SelectDateWidget}


class PropertyForm(forms.ModelForm):
    min_num_rooms = forms.IntegerField()
    max_num_rooms = forms.IntegerField()

    min_price = forms.IntegerField()
    max_price = forms.IntegerField()

    class Meta:
        model = Property
        template_name = 'base/search_property.html'
        exclude = ['images', 'owner', 'price', 'num_rooms', 'adress']
        # widgets = {
        #     'safe_room': forms.HiddenInput(),
        #     'area': forms.HiddenInput(),
        #     'furniture': forms.HiddenInput(),
        #     'elevator': forms.HiddenInput(),
        #     'swimming_pool': forms.HiddenInput(),
        #     'balcony': forms.HiddenInput(),
        #     'renovated': forms.HiddenInput(),
        #     'storage': forms.HiddenInput(),
        #     'disable_access': forms.HiddenInput(),
        #     'central_air_conditioner': forms.HiddenInput(),
        #     'quiet_neighborhood': forms.HiddenInput(),
        #     'posted_date': forms.HiddenInput(),
        #     'images': forms.HiddenInput(),
        #     'clicked_time': forms.HiddenInput()
        # }

