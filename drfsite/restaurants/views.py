from rest_framework import generics
from .models import Restaurants
from .serializer import RestaurantsSerializer


class RestaurantsAPIList(generics.ListCreateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


class RestaurantsAPIUpdate(generics.UpdateAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


class RestaurantsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


# class RestaurantsAPIView(generics.ListAPIView):
#     queryset = Restaurants.objects.all()
#     serializer_class = RestaurantsSerializer
