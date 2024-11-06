from django.conf import settings
from django.db import models
from PIL import Image


class Blog(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    contributors=models.ManyToManyField(settings.AUTH_USER_MODEL, through='BlogContributor', related_name='contributions')
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)

    IMAGE_MAX_SIZE = (800,800)

    def resize_image(self):
        image=Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            self.resize_image()

class BlogContributor(models.Model):
    contributor=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE)
    contribution=models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together=('contributor', 'blog')





