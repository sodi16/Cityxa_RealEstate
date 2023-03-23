from rest_framework import serializers
from .models import Property


class PropertySerializer(serializers.ModelSerializer):
    rent_buy = serializers.CharField(source='display_rent_buy')
    type_of_property = serializers.CharField(source='display_type_of_property')
    class Meta:
        model = Property
        fields = (
            'owner', 'rent_buy', 'type_of_property', 'display_adress', 'price', 'num_rooms', 'description', 'area', 'furniture', 'elevator', 'swimming_pool', 'balcony', 'renovated', 'storage', 'disable_access', 'safe_room', 'central_air_conditioner', 'quiet_neighborhood', 'posted_date'
        )
