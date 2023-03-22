from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django import forms
import datetime

from property.forms import AddAdressForm
from property.models import Property


class LoginForm(LoginView):
    template_name = 'base/login.html'


class RegisterForm(UserCreationForm):
    class Meta:
        YEARS = [x for x in range(1940, datetime.date.today().year)]
        model = get_user_model()
        template_name = 'base/register.html'
        fields = ('username', 'first_name', 'last_name', 'adress', 'birthdate', 'phone_number')
        widgets = {'birthdate': forms.SelectDateWidget(years=YEARS)}
        extra_context = {'adress_form': AddAdressForm}


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        YEARS = [x for x in range(1940, datetime.date.today().year)]
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'adress', 'phone_number', 'birthdate','profil_picture')
        widgets = {'birthdate': forms.SelectDateWidget(years=YEARS)}


class PropertyForm(forms.ModelForm):
    min_num_rooms = forms.IntegerField()
    max_num_rooms = forms.IntegerField()

    min_price = forms.IntegerField()
    max_price = forms.IntegerField()

    class Meta:
        model = Property
        template_name = 'base/search_property.html'
        exclude = ['images', 'owner', 'price', 'num_rooms', 'adress']

