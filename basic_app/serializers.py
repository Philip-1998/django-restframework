from pyexpat import model
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializers):
    class Meta:
        model = Post
        fields = "__all__"