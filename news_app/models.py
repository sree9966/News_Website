from django.db import models
from django.utils import timezone

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    source_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(unique=True)
    url_to_image = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
