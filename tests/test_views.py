import os
import tempfile
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_get(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_view_post_valid_image(self):
        with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
            tmp_file.write(b"dummy image content")
            tmp_file.seek(0)
            image = SimpleUploadedFile(tmp_file.name, tmp_file.read(), content_type="image/jpeg")
            response = self.client.post(reverse('index'), {'image': image})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('index'))

    def test_index_view_post_invalid_file(self):
        with tempfile.NamedTemporaryFile(suffix=".txt") as tmp_file:
            tmp_file.write(b"dummy text content")
            tmp_file.seek(0)
            text_file = SimpleUploadedFile(tmp_file.name, tmp_file.read(), content_type="text/plain")
            response = self.client.post(reverse('index'), {'image': text_file})
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('index'))
            session = self.client.session
            context = session['context']
            self.assertEqual(context['message'], "Not a supported file type. Choose a different image.")

    def test_reset_view_get(self):
        response = self.client.get(reverse('reset_view'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        media_files = os.listdir(settings.MEDIA_ROOT)
        self.assertEqual(len(media_files), 0)

    def test_prediction_history_view_get(self):
        response = self.client.get(reverse('prediction_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'prediction_history.html')
