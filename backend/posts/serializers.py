from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
	class Meta:
		fields = ('id', 'artist', 'title', 'year', 'medium',
				  'substrate', 'size', 'image',)
		model = Post
