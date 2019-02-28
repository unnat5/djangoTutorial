from django.db import models

# Create your models here.
'''
Before making miigration we need to add the app in mysite/settings.py
>> python manage.py makemigrations
to see the actual sql code we could do this 
>> python manage.py sqlmigrate main 0001
and to implement that sql we do this s
>> python manage.py migrate
'''
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length =200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published")

	def __str__(self):
		return self.tutorial_title

