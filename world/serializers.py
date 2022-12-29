from rest_framework import serializers
from .models import Country, State, City

class CountrySerializers(serializers.ModelSerializer):
  class Meta:
    model = Country
    fields = ('url','id','country_name','population')

"""
Used to display Foreign Key in Linked Format
"""
# class StateSerializers(serializers.HyperlinkedModelSerializer):
#   country_id_fk = serializers.HyperlinkedRelatedField( queryset=Country.objects.all(), view_name='country-detail')
#   class Meta:
#     model = State
#     fields = ('url', 'id', 'state_name', 'country_id_fk')

class StateSerializers(serializers.ModelSerializer):
  country_id_fk = serializers.PrimaryKeyRelatedField( queryset=Country.objects.all())
  class Meta:
    model = State
    fields = ('url', 'id', 'state_name', 'country_id_fk')

class CitySerializers(serializers.ModelSerializer):
  state_id_fk = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
  class Meta:
    model = City
    fields = ('url', 'id', 'city_name', 'state_id_fk')

