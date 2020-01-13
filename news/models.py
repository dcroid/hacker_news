from django.db import models


class Post(models.Model):
    title = models.CharField(
        verbose_name='Title News',
        max_length=512,
        blank=False
    )
    url = models.URLField(
        verbose_name='Url News',
        blank=False, null=False, unique=True
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
