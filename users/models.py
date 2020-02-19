from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default_image.jpg', upload_to='profile_pictures')
	date = models.DateTimeField(auto_now=False, null=True, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'
	#overrid the save method for instance user and resize the image for it to be 300 * 300
	def save(self, **kwargs):
		super().save()
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			rezie_image = (300,300)
			img.thumbnail(rezie_image)
			img.save(self.image.path)