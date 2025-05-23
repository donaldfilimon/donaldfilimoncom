from django.urls import path
from .views import index, reset_view, prediction_history

urlpatterns = [
  path("", index, name="index"),
  path('reset', reset_view, name='reset_view'),
  path('prediction-history', prediction_history, name='prediction_history')
]
