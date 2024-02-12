from django.shortcuts import redirect, render
from django.contrib import messages
from projects.models import Project


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
    messages.error(request, "Project could not be activated, try again")
    return redirect("/projects")
  request.session['project_handle'] = handle
  messages.success(request, "project activated")
  return redirect('/')

def deactivate_project_view(request, handle=None):
  delete_project_from_session(request)
  messages.success(request, "project deactivated")
  return redirect('/')