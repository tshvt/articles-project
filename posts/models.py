from django.db import models
from django.utils.text import slugify
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=30, unique=True)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    img_url = models.URLField()
    is_public = models.BooleanField(default=True, null=False)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", null=False, editable=False, unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
