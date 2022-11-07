from django.db import models


class URLMapper(models.Model):
    original_url = models.CharField(max_length=255)
    shortened_url = models.CharField(max_length=255, blank=True)
