from django.test import TestCase
from django.urls import reverse, resolve
from app.views import index, reset_view, prediction_history


class TestUrls(TestCase):
    def test_index_url_resolves(self):
        url = reverse("index")
        self.assertEqual(resolve(url).func.view_class, index.view_class)

    def test_reset_url_resolves(self):
        url = reverse("reset_view")
        self.assertEqual(resolve(url).func.view_class, reset_view.view_class)

    def test_prediction_history_url_resolves(self):
        url = reverse("prediction_history")
        self.assertEqual(resolve(url).func.view_class, prediction_history.view_class)
