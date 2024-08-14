from rest_framework import serializers
from .models import Restaurants


class RestaurantsSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Restaurants
        fields = '__all__'
