import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from multiselectfield import MultiSelectField


def current_year():
	return datetime.date.today().year


def max_value_current_year(value):
	return MaxValueValidator(current_year())(value)


MEDIUMS = ((1, 'Acrylic'),
		   (2, 'Charcoal'),
		   (3, 'Colored Pencil'),
		   (4, 'Gouache'),
		   (5, 'Graphite'),
		   (6, 'Ink'),
		   (7, 'Marker'),
		   (8, 'Oil'),
		   (9, 'Pastel'),
		   (10, 'Pen'),
		   (11, 'Watercolor'))

SUBSTRATES = ((1, 'Canvas'),
			  (2, 'Linen'),
			  (3, 'Panel'),
			  (4, 'Paper'))


class Post(models.Model):
	artist = models.CharField(max_length=20, default='Meredith Bakke', editable=False)
	title = models.CharField(max_length=50)
	year = models.IntegerField(validators=[MinValueValidator(2016), max_value_current_year])
	medium = MultiSelectField(choices=MEDIUMS)
	substrate = MultiSelectField(choices=SUBSTRATES)
	size = models.CharField(max_length=10)
	image = models.ImageField(upload_to='images/')

	def __str__(self):
		return self.title
