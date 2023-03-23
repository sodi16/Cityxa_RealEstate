from django.urls import path, include
from property.views import add_property, display_property, search_property, DeletePropertyView, UpdatePropertyView, api_property_list



urlpatterns = [
    path('add_property/', add_property, name='add_property'),
    path('<int:pk>/', display_property.as_view(), name='display_property'),
    path('delete-<int:pk>/', DeletePropertyView.as_view(), name='delete_property'),
    path('update-<int:pk>/', UpdatePropertyView.as_view(), name='update_property'),
    path('search/', search_property, name='search_property'),
    path('api/', api_property_list)
]
