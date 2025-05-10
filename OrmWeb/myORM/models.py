from django.db import models
from django.contrib import admin

class Movie(models.Model):
	TITLE=models.CharField(max_length=50)
	GENRE=models.CharField(max_length=30)
	RELEASE_DATE=models.DateField()
	RATING=models.FloatField()

class MovieAdmin(admin.ModelAdmin):
	list_display=('TITLE','GENRE','RELEASE_DATE','RATING')
