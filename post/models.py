from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100, unique=True, blank=True, null=True)
	image = models.URLField(blank=True, null=True, unique=True)
	content = models.TextField(blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)
