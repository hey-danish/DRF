from world.views import CountryViewSet, StateViewSet, CityViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from world import views

router = SimpleRouter()
router.register(r'country', views.CountryViewSet, basename="country" )
router.register(r'state', views.StateViewSet, basename='state')
router.register(r'city', views.CityViewSet, basename='city')
#urlpatterns = router.urls

urlpatterns = [
  path('', views.world_root, name='world_root'),
  path('v1.0/', include(router.urls))
]

