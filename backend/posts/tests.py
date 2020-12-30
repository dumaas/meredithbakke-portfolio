from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostTest(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Create user
		testuser1 = User.objects.create_user(
			username='testuser1', password='abc123')
		testuser1.save()

		# Create post post
		test_post = Post.objects.create(
			title='Artwork title', year='2020',
			size='32x64', image='test_image.jpg')
		test_post.save()

	def test_post_content(self):
		post = Post.objects.get(id=1)
		title = f'{post.title}'
		year = f'{post.year}'
		size = f'{post.size}'
		image = f'{post.image}'

		self.assertEqual(title, 'Artwork title')
		self.assertEqual(year, '2020')
		self.assertEqual(size, '32x64')
		self.assertEqual(image, 'test_image.jpg')
