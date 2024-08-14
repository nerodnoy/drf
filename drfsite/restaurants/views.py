from rest_framework import generics, viewsets
from .models import Restaurants
from .serializer import RestaurantsSerializer


# Заменяет весь CRUD
# Наследование от ModelViewSet или ReadOnlyModelViewSet
class RestaurantsViewSet(viewsets.ModelViewSet):
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer


# class RestaurantsAPIList(generics.ListCreateAPIView):
#     queryset = Restaurants.objects.all()
#     serializer_class = RestaurantsSerializer
#
#
# class RestaurantsAPIUpdate(generics.UpdateAPIView):
#     queryset = Restaurants.objects.all()
#     serializer_class = RestaurantsSerializer
#
#
# class RestaurantsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurants.objects.all()
#     serializer_class = RestaurantsSerializer
