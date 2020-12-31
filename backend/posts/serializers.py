from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'artist', 'title', 'year', 'medium',
				  'substrate', 'size', 'image',)
		model = Post


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username',)
