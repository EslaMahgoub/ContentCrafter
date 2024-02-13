from .models import Project
from django import forms


class ProjectCreateForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'handle']

class ProjectUpdateForm(forms.ModelForm):
  class Meta:
    model = Project
    fields = ['title', 'description', 'handle']
