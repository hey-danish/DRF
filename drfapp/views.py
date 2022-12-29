from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def app_root( request, format=None):
  return Response({
    'bookstore': reverse('bookstore_root', request=request, format=format),
    'snippet': reverse('snippets_root', request=request, format=format),
    'world':reverse('world_root', request=request, format=format),
    'touristmap': reverse( 'touristmap' , request=request, format=format),
  })