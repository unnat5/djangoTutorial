from django.db import models
from django.utils import timezone

# Create your models here.
'''
Before making migration we need to add the app in mysite/settings.py
>> python manage.py makemigrations
to see the actual sql code we could do this 
>> python manage.py sqlmigrate main 0001
and to implement that sql we do this 
>> python manage.py migrate
'''


class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200)


	class Meta:
		# Gives the proper plural name of admin
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory,default=1,verbose_name = "Category",
		on_delete = models.SET_DEFAULT)
	series_summary = models.CharField(max_length=200)
	class Meta:
		# otherwise we get "Tutorial Seriess in admin"
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series



class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length =200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default = timezone.now())

	tutorial_series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series",
		on_delete = models.SET_DEFAULT)
	#https://docs.djangoproject.com/en/2.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
	tutorial_slug = models.CharField(max_length=200, default=1)

	def __str__(self):
		return self.tutorial_title

