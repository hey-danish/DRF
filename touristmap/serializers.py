from rest_framework import serializers
from touristmap.models import Places, PlaceAttributes, TravelAgents


class PlacesSerializers(serializers.ModelSerializer):
  address = serializers.CharField(required=True)
  class Meta:
    model = Places
    fields = "__all__"


class PlaceAttributesSerializers(serializers.ModelSerializer):
  class Meta:
    model = PlaceAttributes
    fields = "__all__"


class TravelAgentsSerializers(serializers.ModelSerializer):
  class Meta:
    model = TravelAgents
    fields = "__all__"