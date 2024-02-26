from django_htmx.http import trigger_client_event
from django.http import HttpResponse

def render_refresh_list(request, response_text=""):
  custom_refresh_event = "refresh-list-view"
  response = HttpResponse(response_text)
  return trigger_client_event(response, custom_refresh_event)