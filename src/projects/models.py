from django.conf import settings
from django.db import models
from django.urls import reverse
from config.utils.generators import unique_slugify
from . import validators

User = settings.AUTH_USER_MODEL

class AnonymousProject():
  value = None
  is_activated = False

class Project(models.Model):
  owner = models.ForeignKey(User, null=True, related_name="projects_owned", on_delete=models.SET_NULL)
  title = models.CharField(max_length=120, null=True)
  description = models.TextField(blank=True, null=True)
  handle = models.SlugField(null=True, blank=True, unique=True, validators=[validators.validate_project_handle])
  added_by = models.ForeignKey(User, related_name="projects_added", on_delete=models.SET_NULL, null=True)
  added_by_username = models.CharField(max_length=120, blank=True, null=True)
  last_modifited_by = models.ForeignKey(User, related_name="projects_changed", on_delete=models.SET_NULL, null=True)
  active = models.BooleanField(default=True)
  updated = models.DateTimeField(auto_now_add=False, auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
  
  @property
  def is_activated(self):
    return True
  
  class Meta:
    ordering = ('title',)

  def __str__(self):
    return self.title

  def save(self, *args, **kwargs):
    if self.added_by:
      self.added_by_username = self.added_by.username
    if self.title:
      self.handle = unique_slugify(self, slug_field='handle', invalid_slug='create')
    super().save(*args, **kwargs)

  def get_absolute_url(self):
      return reverse("projects:detail", kwargs={"handle": self.handle})
  
  def get_delete_url(self):
      return reverse("projects:delete", kwargs={"handle": self.handle})
  
  def get_activate_url(self):
      return reverse("projects:activate_project", kwargs={"handle": self.handle})