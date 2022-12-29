from bookstore.models import Books, Authors, Publishers
from bookstore.serializers import BooksSerializer, AuthorsSerializers, PublishersSerializer
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response


@api_view(['GET'])
def bookstore_root( request, format=None):
  return Response({
    'books': reverse('books-list', request=request, format=format),
    'authors':reverse('authors-list', request=request, format=format),
    'publications':reverse('publications-list', request=request, format=format)
  })

# Create your views here.
class BooksList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Books.objects.all()
  serializer_class = BooksSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class BooksDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Books.objects.all()
  serializer_class = BooksSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


# Create your views here.
class AuthorsList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Authors.objects.all()
  serializer_class = AuthorsSerializers

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class AuthorsDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Authors.objects.all()
  serializer_class = AuthorsSerializers

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)


# Create your views here.
class PublishersList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
  queryset = Publishers.objects.all()
  serializer_class = PublishersSerializer

  def get(self, request, *args, **kwargs):
    return self.list(request, *args, **kwargs)

  def post(self, request, *args, **kwargs):
    return self.create(request, *args, **kwargs)


class PublishersDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  queryset = Publishers.objects.all()
  serializer_class = PublishersSerializer

  def get(self, request, *args, **kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self, request, *args, **kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self, request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)

