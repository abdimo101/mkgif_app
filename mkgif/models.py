from django.db import models

# Create your models here.

class Animation(models.Model):
      name = models.CharField(max_length=200)


class Image(models.Model):
      def image_path(self, filename):
          return f'{self.animation.pk}/{filename}'

      animation = models.ForeignKey('Animation', on_delete=models.CASCADE)
      image = models.ImageField(upload_to=image_path)
