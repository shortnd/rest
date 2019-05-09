from .models import Post
from rest_framework import serializers

class PostSerializers(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Post
    fields = ('title', 'body', 'user')