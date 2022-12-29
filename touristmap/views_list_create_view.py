from touristmap.models import PlaceAttributes, Places
from rest_framework.generics import CreateAPIView, ListAPIView
from touristmap.serializers import PlacesSerializers, PlaceAttributesSerializers

class PlaceAttributesCreateAPIView(CreateAPIView):
  serializer_class = PlaceAttributesSerializers

  def perform_create(self, serializer):
    return serializer.save( )

class PlaceAttributesListAPIView(ListAPIView):
  serializer_class = PlaceAttributesSerializers

  def get_queryset(self):
    return PlaceAttributes.objects.all()

class PlacesCreateAPIView(CreateAPIView):
  serializer_class = PlacesSerializers
  def perform_create(self, serializer):
    return serializer.save( )

class PlacesListAPIView(ListAPIView):
  serializer_class = PlacesSerializers

  def get_queryset(self):
    return Places.objects.all()
