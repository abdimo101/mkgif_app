from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animation(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      name = models.CharField(max_length=200)
      

class Image(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      def image_path(self, filename):
          return f'{self.animation.pk}/{filename}'

      animation = models.ForeignKey(Animation, on_delete=models.CASCADE)
      image = models.ImageField(upload_to=image_path)
