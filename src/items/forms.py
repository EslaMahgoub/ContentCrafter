from .models import Item
from django import forms


class ItemCreateForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['title']

class ItemUpdateForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['title', 'status', 'description']
    

class ItemInlineForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['title', 'status']

class ItemPatchForm(forms.Form):
  title = forms.CharField(required=False)
  status = forms.CharField(required=False)