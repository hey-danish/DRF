from rest_framework import serializers
from bookstore.models import Books, Publishers, Authors

class BooksSerializer(serializers.HyperlinkedModelSerializer):
  authors = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all(), many=True)
  publisher_partners = serializers.PrimaryKeyRelatedField(queryset=Publishers.objects.all(), many=True)

  class Meta:
    model = Books
    fields = ['id', 'book_title', 'genre', 'isn_number',
              'authors', 'publisher_partners', 'publication_date']


class PublishersSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Publishers
    fields = ['id','url', 'publisher_name', 'address', 'publisher_email']


class AuthorsSerializers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Authors
    fields = ['id','url','author_name','country','gender','email','mobile','onboarding_date']
