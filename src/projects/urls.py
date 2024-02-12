from django.urls import path
from . import views
urlpatterns = [
    path('activate/<slug:handle>', views.activate_project_view),
    path('deactivate/<slug:handle>', views.deactivate_project_view),
]
