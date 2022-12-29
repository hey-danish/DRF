from django.urls import path
from touristmap.views import PlaceAttributesListAPIView, PlaceAttributesCreateAPIView, PlacesCreateAPIView, PlacesListAPIView

urlpatterns = [
    path('placeattributes-list/', PlaceAttributesListAPIView.as_view(),name='placeattributes-list'),
    path('placeattributes-create/', PlaceAttributesCreateAPIView.as_view(), name='placeattributes-create'),
    path('places-list/', PlacesListAPIView.as_view(), name='places-list'),
    path('places-create/', PlacesCreateAPIView.as_view(), name='places-create'),
]

