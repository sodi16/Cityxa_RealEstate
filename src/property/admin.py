from django.contrib import admin
from django.contrib.auth import get_user
from property.models import Property


class AllPropertiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner', 'id_rent_buy', 'id_type_of_property', 'adress', 'price', 'num_rooms', 'area', 'furniture', 'elevator', 'swimming_pool', 'balcony', 'renovated', 'storage', 'disable_access', 'safe_room', 'central_air_conditioner', 'quiet_neighborhood', 'posted_date', 'clicked_time')


# class AllPropertyAdmin():
# admin.site.register(Property, AllPropertyAdmin)

admin.site.register(Property, AllPropertiesAdmin)
