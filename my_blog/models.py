from django.db import models
from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('post_details', kwargs= {'pk': self.pk})
	

