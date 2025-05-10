# Ex02 Django ORM Web Application
## Date: 10-05-2025

## AIM
To develop a Django application to store and retrieve data from a Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 Movies

## PROGRAM

admin.py

```
from django.contrib import admin
from .models import Movie,MovieAdmin

admin.site.register(Movie,MovieAdmin)
```

models.py

```
from django.db import models
from django.contrib import admin

class Movie(models.Model):
	TITLE=models.CharField(max_length=50)
	GENRE=models.CharField(max_length=30)
	RELEASE_DATE=models.DateField()
	RATING=models.FloatField()

class MovieAdmin(admin.ModelAdmin):
	list_display=('TITLE','GENRE','RELEASE_DATE','RATING')

```


## OUTPUT

Name: Arunsamy D
Reg no: 212224240016 / 24900591

![alt text](<Screenshot (82).png>)

## RESULT
Thus the program for creating movies database using ORM hass been executed successfully
