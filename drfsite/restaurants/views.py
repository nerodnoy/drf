from rest_framework import generics
from .models import Restaurants
from .serializer import RestaurantsSerializer


class RestaurantsAPIView(generics.ListAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer
