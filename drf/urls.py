from django.urls import path, include
from rest_framework.routers import SimpleRouter
from drf.views import StudentModelViewSet


router = SimpleRouter()
router.register(r'student', StudentModelViewSet, basename='student')

urlpatterns = router.urls
