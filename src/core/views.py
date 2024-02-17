from django.shortcuts import render
from items.models import Item
from projects.decorators import project_required


@project_required
def dashboard_view(request):
  qs = Item.objects.filter(project=request.project)
  return render(request, "dashboard/home.html",{"items_list": qs}) 

def index(request):
  if not request.user.is_authenticated:
    return render(request, 'core/index.html', {})
  return dashboard_view(request)

def about(request):
  return render(request, 'core/about.html', {})