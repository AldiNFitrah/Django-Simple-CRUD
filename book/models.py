from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    cover = models.ImageField(upload_to='static/books/covers/', null=True, blank=True)
