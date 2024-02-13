from django.urls import path
from . import views

app_name = "items"
urlpatterns = [
    path("create/", views.item_create_view, name="create"),
]
