from django.contrib.auth import authenticate, login, logout, get_user_model, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView, UpdateView
from users.models import User
from users.forms import RegisterForm


def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'users/register.html', {'form': form})


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
    form_class = RegisterForm
    # fields = ['first_name', 'last_name', 'username', 'adress', 'phone_number', 'birthdate']
    template_name = 'users/update_profile.html'
    context_object_name = 'form'
