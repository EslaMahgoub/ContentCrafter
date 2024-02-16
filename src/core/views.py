from django.shortcuts import render
from items.models import Item

def index(request):
  if not request.user.is_authenticated:
    return render(request, 'core/index.html', {})
  
  qs = Item.objects.filter(project=request.project)
  return render(request, "dashboard/home.html", {"items_list": qs})


def about(request):
  return render(request, 'core/about.html', {})