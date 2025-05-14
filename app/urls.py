from django.urls import path
from .views import index, reset_view

urlpatterns = [
  path("", index, name="index"),
  path('reset', reset_view, name='reset_view')
]