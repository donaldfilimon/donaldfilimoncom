from django.urls import path
from .views import index, reset_view, prediction_history

# URL patterns for the app
urlpatterns = [
    path("", index, name="index"),  # Home page
    path("reset", reset_view, name="reset_view"),  # Reset view
    path("prediction-history", prediction_history, name="prediction_history"),  # Prediction history view
]
