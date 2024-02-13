from django.urls import reverse

def site_urls(request):
  project_create_url = reverse("projects:create")
  deactivate_project_url = reverse("projects:deactivate_project")
  projects_list_url = reverse("projects:list")
  return {
    "home_url": reverse("home"),
    "about_url": reverse("about"),
    "project_create_url": project_create_url,
    "deactivate_project_url": deactivate_project_url,
    "projects_list_url": projects_list_url,
  }