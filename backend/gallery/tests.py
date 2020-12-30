from django.test import TestCase
from django.contrib.auth.models import User
from .models import Gallery


class GalleryTests(TestCase):

	@classmethod
	def setUpTestData(cls):
		# Create user
		testuser1 = User.objects.create_user(
			username='testuser1', password='abc123')
		testuser1.save()

		# Create gallery post
		test_post = Gallery.objects.create(
			title='Artwork title', year='2020',
			size='32x64', image='test_image.jpg')
		test_post.save()

	def test_gallery_content(self):
		gallery = Gallery.objects.get(id=1)
		title = f'{gallery.title}'
		year = f'{gallery.year}'
		size = f'{gallery.size}'
		image = f'{gallery.image}'

		self.assertEqual(title, 'Artwork title')
		self.assertEqual(year, '2020')
		self.assertEqual(size, '32x64')
		self.assertEqual(image, 'test_image.jpg')
