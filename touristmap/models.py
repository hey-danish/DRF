from django.db import models
from world.models import Country, State, City

PLACE_CATEGORY = (
  ('ML', 'Mall'),
  ('PK', 'Park'),
  ('MU', 'Museum'),
  ('WP', 'Water Park'),
  ('GO', 'Government Office'),
  ('AH', 'Ancient Heritage'),
  ('OT', 'Others')
)

TRANSPORTATION_MEDIUM_OPTIONS = (
  ('TR', 'Train'),
  ('BS', 'Bus'),
  ('AB', 'Airbus'),
  ('YC', 'Yatch')
)

# Create your models here.

class PlaceAttributes(models.Model):
  attr_name = models.CharField(max_length=100, blank=False)

  def __str__(self):
    return self.attr_name



class Places(models.Model):
  place_title = models.CharField(max_length=100, blank=False, null=False, default='Unknown')
  place_category = models.CharField(max_length=10, choices=PLACE_CATEGORY, null=False, blank=False)
  address = models.CharField(max_length=200, blank=True)
  attributes = models.ManyToManyField(PlaceAttributes, null=False, blank=False)
  is_public_allowed = models.BooleanField(default=False, blank=False)
  city = models.ForeignKey(City, on_delete=models.CASCADE, blank=False)
  state = models.ForeignKey(State, on_delete=models.CASCADE, blank=False)
  country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)


  def __str__(self):
    return self.park_title


class TravelAgents(models.Model):
  agent_name = models.CharField(max_length=150, blank=False, null=False)
  city_coverage = models.ManyToManyField( City, blank=False )
  country_coverage = models.ManyToManyField( Country, blank=False )
  transportation_medium = models.CharField(max_length=20, choices=TRANSPORTATION_MEDIUM_OPTIONS, blank=False)
  is_international_agent = models.BooleanField(default=False, blank=False)
  is_active = models.BooleanField( blank=False, default=True )

  def __str__(self):
    return self.agent_name




