from rest_framework import serializers
from .models import Restaurants


class RestaurantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('title', 'cat_id')
