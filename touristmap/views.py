from touristmap.models import PlaceAttributes, Places, TravelAgents
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from touristmap.serializers import PlacesSerializers, PlaceAttributesSerializers, TravelAgentsSerializers
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework import mixins

class TouristMapRoot( GenericAPIView ):
  name = 'Tourist Map'
  def get(self, request, *args, **kwargs):
    return Response({
      'places': reverse(PlacesAPIView.name, request=request),
      'placeattribute': reverse(PlaceAttibutesAPIView.name, request = request),
      'travel-agent': reverse(TravelAgentCreateList.name, request=request),
    })


class PlacesAPIView(ListCreateAPIView):
  serializer_class = PlacesSerializers
  name = 'places-list'

  def perform_create(self, serializer):
    return serializer.save( )

  def get_queryset(self):
    return Places.objects.all()


class PlacesDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class = PlacesSerializers
  lookup_field = "id"
  name = 'places-detail'

  def get_queryset(self):
    return Places.objects.all()


class PlaceAttibutesAPIView(ListCreateAPIView):
  serializer_class = PlaceAttributesSerializers
  name = 'placeattributes-list'

  def perform_create(self, serializer):
    return serializer.save( )

  def get_queryset(self):
    return PlaceAttributes.objects.all()


class PlaceAttributesDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class = PlaceAttributesSerializers
  lookup_field = "id"
  name = 'placeattributes-detail'

  def get_queryset(self):
    return PlaceAttributes.objects.all()


class TravelAgentCreateList( mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView ):
  serializer_class = TravelAgentsSerializers
  queryset = TravelAgents.objects.all()
  name='travel-agent-list'

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)




class TravelAgentDetail( mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView ):
  serializer_class = TravelAgentsSerializers
  queryset = TravelAgents.objects.all()
  lookup_field = "id"
  name='travel-agent-detail'

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def patch(self, request, *args, **kwargs):
      return self.partial_update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)
