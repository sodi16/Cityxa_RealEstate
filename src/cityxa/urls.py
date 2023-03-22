from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from cityxa.views import home
from users.views import register, Login
from cityxa import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('login/', Login.as_view(), name='login'),
    path('register/', register, name='register'),
    path('user/', include('users.urls')),
    path('property/', include('property.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
