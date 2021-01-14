from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class PostTests(TestCase):

  @classmethod
  def setUpTestData(cls):
    # Create user
    testuser1 = User.objects.create_user(
        username='testuser1',
        password='abc123')
    testuser1.save()

    # Create post post
    test_post = Post.objects.create(
        author=testuser1,
        title='Artwork title',
        year='2020',
        medium="oil",
        substrate="canvas",
        size='32x64',
        image='test_image.jpg')
    test_post.save()

  def test_post_content(self):
    post = Post.objects.get(id=1)
    author = f'{post.author}'
    title = f'{post.title}'
    year = f'{post.year}'
    medium = f'{post.medium}'
    substrate = f'{post.substrate}'
    size = f'{post.size}'
    image = f'{post.image}'

    self.assertEqual(author, 'testuser1')
    self.assertEqual(title, 'Artwork title')
    self.assertEqual(year, '2020')
    self.assertEqual(medium, 'oil')
    self.assertEqual(substrate, 'canvas')
    self.assertEqual(size, '32x64')
    self.assertEqual(image, 'test_image.jpg')
