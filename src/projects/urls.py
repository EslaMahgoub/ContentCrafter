from django.urls import path
from . import views

app_name = "projects"

urlpatterns = [
    path("", views.project_list_view, name="list"),
    path("create/", views.project_create_view, name="create"),
    path('deactivate/', views.deactivate_project_view, name="deactivate_project"),
    path("<slug:handle>/", views.project_detail_update_view, name="detail"),
    path("<slug:handle>/delete/", views.project_delete_view, name="delete"),
    path('activate/<slug:handle>/', views.activate_project_view, name="activate_project"),
]
