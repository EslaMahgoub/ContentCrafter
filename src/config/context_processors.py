from django.urls import reverse

def site_urls(request):
  project_create_url = reverse("projects:create")
  projects_list_url = reverse("projects:list")
  item_create_url = reverse("items:create")
  items_list_url = reverse("items:list")
  deactivate_project_url = reverse("projects:deactivate_project")
  return {
    "home_url": reverse("home"),
    "about_url": reverse("about"),
    "project_create_url": project_create_url,
    "deactivate_project_url": deactivate_project_url,
    "projects_list_url": projects_list_url,
    "item_create_url": item_create_url,
    "items_list_url": items_list_url,
  }