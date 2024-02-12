from typing import Iterable
from django.conf import settings
from django.db import models
from config.utils.generators import unique_slugify

User = settings.AUTH_USER_MODEL

class Project(models.Model):
  owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
  title = models.CharField(max_length=120, null=True)
  handle = models.SlugField(null=True, blank=True, unique=True)
  active = models.BooleanField(default=True)
  updated = models.DateTimeField(auto_now_add=False, auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

  class Meta:
    ordering = ('title',)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if self.title:
      self.handle = unique_slugify(self, slug_field='handle')
    super().save(*args, **kwargs)