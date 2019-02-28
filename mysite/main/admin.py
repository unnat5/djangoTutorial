from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE ## import TinyMCE for textfield
from django.db import models  ## import models to modify textField.

'''
To access our site in admin page we need to register it here.
'''

## Customization admin page
'''
class TutorialAdmin(admin.ModelAdmin):
	fields = ["tutorial_published","tutorial_title","tutorial_content",]
	## changing the order of the fields.
'''
## we can cluster similar fields together
class TutorialAdmin(admin.ModelAdmin):

	fieldsets= [
		("Title/date",{"fields":["tutorial_title","tutorial_published"]}),
		("Content", {"fields":["tutorial_content"]}),
	]

	## modifying the textfield so have nice editor in it.
	formfield_overrides = {
		models.TextField: {'widget':TinyMCE()}

	}

# Register your models here.
admin.site.register(Tutorial,TutorialAdmin)


