from django.db import models

# Create your models here.

GENDER_CHOICES = (
  ("NS","Not Set"),
  ("ML","Male"),
  ("FM","Female"),
  ("TS","Transgender")
)

GENRE_CHOICES = (
  ("IF","Infotainment"),
  ("EN","Entertainment"),
  ("HR","Horror"),
  ("BG","Biography"),
  ("SF","Scifi")
)

class Authors(models.Model):
  author_name = models.CharField(max_length=100, blank=False)
  country = models.CharField(max_length=100, blank=False)
  gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='NS', blank=False)
  email = models.CharField(max_length=25, blank=True)
  mobile = models.CharField(max_length=45, blank=True)
  onboarding_date = models.DateField(blank=False)

  def __str__(self):
    return self.author_name


class Publishers(models.Model):
  publisher_name = models.CharField(max_length=150, blank=False)
  address = models.CharField(max_length=250, blank=True)
  publisher_email = models.CharField(max_length=150, blank=True)

  def __str__(self):
    return self.publisher_name


class Books(models.Model):
  book_title = models.CharField(max_length=100, blank=False)
  genre = models.CharField(max_length=20, choices=GENRE_CHOICES, blank=False)
  isn_number = models.CharField(max_length=200, blank=True)
  authors = models.ManyToManyField(Authors, blank=False)
  publisher_partners = models.ManyToManyField(Publishers, blank=True)
  publication_date = models.DateField(blank=False)

  def __str__(self):
    return self.book_title




