from django.contrib import admin
from .models import NewsArticle

admin.site.register(NewsArticle)
admin.site.site_url = '/news/'


# Register your models here.
