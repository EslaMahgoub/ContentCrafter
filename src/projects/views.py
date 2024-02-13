from django.shortcuts import redirect, render
from django.contrib import messages
from projects.models import Project

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms

PROJECT_CAN_DELETE_ITEM_THRESHOLD = 2

@login_required
def project_list_view(request):
  object_list = Project.objects.filter(owner=request.user)
  return render(request, 'projects/list.html', {"object_list": object_list})

@login_required
def project_detail_update_view(request, handle=None):
  instance = get_object_or_404(Project, handle=handle, owner=request.user)
  items_qs = instance.item_set.all()
  form = forms.ProjectUpdateForm(request.POST or None, instance=instance)
  if form.is_valid():
    project_obj = form.save(commit=False)
    project_obj.last_modifited_by = request.user
    project_obj.save()
    return redirect(project_obj.get_absolute_url())
  context = {
    "instance": instance, 
    "form": form,
    "items_qs": items_qs
  }
  return render(request, 'projects/detail.html', context)

@login_required
def project_create_view(request):
  if not request.project.is_activated:
    return render(request, 'project.activate.html', {})
  form = forms.ProjectCreateForm(request.POST or None)
  if form.is_valid():
    project_obj = form.save(commit=False)
    project_obj.owner = request.user
    project_obj.added_by = request.user
    project_obj.save()
    return redirect(project_obj.get_absolute_url())
  return render(request, 'projects/create.html', {"form": form})


@login_required
def project_delete_view(request, handle=None):
  instance = get_object_or_404(Project, handle=handle, owner=request.user)
  items_qs = instance.item_set.all()
  items_count = items_qs.count()
  items_exists = items_qs.exists()
  if request.method == "POST":
    if items_exists and items_count >= PROJECT_CAN_DELETE_ITEM_THRESHOLD:
      messages.error(request, f"Cannot delete project with {PROJECT_CAN_DELETE_ITEM_THRESHOLD} or more active items")
      return redirect(instance.get_delete_url())
    instance.delete()
    return redirect("projects:list")
  return render(request, "projects/delete.html", {"instance":instance})

def delete_project_from_session(request):
  try:
    del request.session['project_handle'] 
  except:
    pass

def activate_project_view(request, handle=None):
  #http://127.0.0.1:8000/projects/activate/content-crafter
  try:
    project_obj  = Project.objects.get(owner=request.user, handle=handle)
  except:
    project_obj = None

  if project_obj is None:
    delete_project_from_session(request)
    messages.error(request, "Project could not be activated, please try again")
    return redirect("/projects")
  request.session['project_handle'] = handle
  messages.success(request, "Project activated Successfully")
  return redirect('/')

def deactivate_project_view(request, handle=None):
  delete_project_from_session(request)
  messages.success(request, "Project deactivated Successfully")
  return redirect('/')

