
from django.urls import path, include
from touristmap.views import TouristMapRoot, TravelAgentCreateList, TravelAgentDetail, PlaceAttibutesAPIView, \
    PlacesAPIView, \
    PlaceAttributesDetailAPIView, PlacesDetailAPIView


urlpatterns = [
    path('', TouristMapRoot.as_view(), name='touristmap' ),
    path('places/', PlacesAPIView.as_view(), name='places-list'),
    path('places/<int:id>', PlacesDetailAPIView.as_view() ),
    path('placeattributes/', PlaceAttibutesAPIView.as_view(), name='placeattributes-list'),
    path('placeattributes/<int:id>', PlaceAttributesDetailAPIView.as_view()),
    path('travel-agent/', TravelAgentCreateList.as_view(), name='travel-agent-list' ),
    path('travel-agent/<int:id>/', TravelAgentDetail.as_view(), name='travel-agent-detail' )
]


