from django.urls import path, include
from django.contrib.auth.views import LogoutView
from users.views import profil, ProfilView, UpdateProfilView


urlpatterns = [
    path('logout/', LogoutView.as_view(template_name='users/base.html'), name='logout'),
    path('profil-<int:pk>', ProfilView.as_view(), name='profil_page'),
    path('update-<int:pk>', UpdateProfilView.as_view(), name='update_profile')
]
