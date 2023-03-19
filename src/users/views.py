from django.contrib.auth import authenticate, login, logout, get_user_model, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView

from property.forms import AddAdressForm
from users.models import User
from users.forms import RegisterForm, UpdateProfileForm, AddAdressForm


def register(request):
    form = RegisterForm()
    adress_form = AddAdressForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            adress = AddAdressForm(request.POST)
            if adress.is_valid():
                adress = adress.save()
                user.adress = adress
                user.save()
            login(request, user)
            return redirect('home')
    return render(request, 'users/register.html', {'form': form, 'adress_form': adress_form})


class Login(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required
def profil(request):
    user = get_user(request)
    context = {'user': user}
    return render(request, 'users/profil.html', context)


class ProfilView(DetailView):
    model = get_user_model()
    context_object_name = 'user'
    template_name = 'users/profil.html'


class UpdateProfilView(UpdateView):
    model = User
    form_class = UpdateProfileForm
    # fields = ['first_name', 'last_name', 'username', 'adress', 'phone_number', 'birthdate']
    template_name = 'users/update_profile.html'
    context_object_name = 'form'
    extra_context = {'adress_form': AddAdressForm}

