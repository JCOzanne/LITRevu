from django.conf import settings
from django.db import models
from PIL import Image



class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (800,800)

    def resize_image(self):
        image=Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()




