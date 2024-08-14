from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Restaurants, Category
from .serializer import RestaurantsSerializer


# Заменяет весь CRUD
# Наследование от ModelViewSet или ReadOnlyModelViewSet
class RestaurantsViewSet(viewsets.ModelViewSet):
    # Если мы убираем отсюда queryset, то нам нужно добавить basename в routes
    queryset = Restaurants.objects.all()
    serializer_class = RestaurantsSerializer

    # Можем переопределять метод queryset, чтобы получать сложное поведение
    # def get_queryset(self):
    #     pk = self.kwargs.get("pk")
    #     if not pk:
    #         return Restaurants.objects.all()[:3]
    #
    #     return Restaurants.objects.filter(pk=pk)

    # Если нам нужно больше маршрутов добавить
    # Если detail=False, то выведем все записи
    @action(methods=['get'], detail=False)
    # Имя маршрута будет формироваться от имени этого метода ниже
    def category(self, request):
        categories = Category.objects.all()
        return Response({'categories': [c.name for c in categories]})

    # Если detail=True, то выведем только одну запись
    @action(methods=['get'], detail=True)
    def categories(self, request, pk=None):
        categories = Category.objects.get(pk=pk)
        return Response({'categories': categories.name})


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
