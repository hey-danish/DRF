from world.serializers import CountrySerializers, StateSerializers, CitySerializers
from world.models import Country, State, City
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def world_root( request, format=None):
  return Response({
    'country': reverse('country-list', request=request, format=format),
    'state': reverse('state-list', request=request, format=format),
    'city': reverse('city-list', request=request, format=format),
  })


class CountryViewSet( viewsets.ModelViewSet ):
  queryset = Country.objects.all()
  serializer_class = CountrySerializers
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

class StateViewSet( viewsets.ModelViewSet ):
  queryset = State.objects.all()
  serializer_class = StateSerializers

class CityViewSet( viewsets.ModelViewSet ):
  queryset = City.objects.all()
  serializer_class = CitySerializers
