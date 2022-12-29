from django.db import models
from world.models import City

class Student(models.Model):
  name = models.CharField(max_length=100, blank=False)
  roll = models.IntegerField(blank=False)
  city = models.ForeignKey(City, blank=False, null=False, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

# Create your models here.
