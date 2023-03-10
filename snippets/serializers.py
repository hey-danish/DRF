from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User

class SnippetsSerializers(serializers.HyperlinkedModelSerializer):
  owner = serializers.ReadOnlyField(source='owner.username')
  highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

  class Meta:
    model = Snippet
    fields = ('url','id','title','code','linenos','language','style','owner','highlight')


class UserSerializer(serializers.ModelSerializer):
  snippets = serializers.PrimaryKeyRelatedField( many = True, queryset=Snippet.objects.all() )

  class Meta:
    model = User
    fields = ('url','id','username','snippets')

