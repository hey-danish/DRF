from django.db import models

# Create your models here.
class Country(models.Model):
  country_name = models.CharField(max_length=100, blank=False)
  population = models.IntegerField(blank=False)

  def __str__(self):
    return self.country_name

class State(models.Model):
  state_name = models.CharField(max_length=100, blank=False)
  country_id_fk = models.ForeignKey(Country, blank=False, on_delete=models.CASCADE)

  def __str__(self):
    return self.state_name

class City(models.Model):
  city_name = models.CharField(max_length=100, default=False)
  state_id_fk = models.ForeignKey(State, on_delete=models.CASCADE, blank=False)

  def __str__(self):
    return self.city_name



