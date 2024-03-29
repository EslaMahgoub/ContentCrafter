from django.db import models
from django.urls import reverse

# Create your models here.
from projects.models import Project
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

class Item(models.Model):
  class ItemStatus(models.TextChoices):
    PUBLISH = 'publish', 'Publish'
    PENDING = 'pending', 'Pending'
    DRAFT = 'draft', 'Draft'
    ON_HOLD = 'on_hold', 'On Hold'
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  status = models.CharField(max_length=20, choices=ItemStatus.choices, default=ItemStatus.DRAFT)
  _status = models.CharField(max_length=20, choices=ItemStatus.choices, blank=True, null=True)
  status_changed_at = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
  added_by = models.ForeignKey(User, related_name="items_added", on_delete=models.SET_NULL, null=True)
  added_by_username = models.CharField(max_length=120, blank=True, null=True)
  last_modifited_by = models.ForeignKey(User, related_name="items_changed", on_delete=models.SET_NULL, null=True)
  title = models.CharField(max_length=120)
  description = models.TextField(blank=True, null=True)
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return self.title
  
  def save(self, *args, **kwargs):
    if self.added_by:
      self.added_by_username = self.added_by.username
    if self._status != self.status:
      self._status = self.status
      self.status_changed_at = timezone.now()
    super().save(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("items:detail", kwargs={"id": self.id})
    
  def get_delete_url(self):
    return reverse("items:delete", kwargs={"id": self.id})
    
  def get_edit_url(self):
    return reverse("items:edit", kwargs={"id": self.id})
  