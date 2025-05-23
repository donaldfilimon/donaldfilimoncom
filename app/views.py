from pathlib import Path
import cv2
import numpy as np
import logging

from PIL import Image
from keras.models import load_model

from django.http import HttpResponseServerError
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.views.generic import base

logger = logging.getLogger('django')

class CustomFileSystemStorage(FileSystemStorage):
  def get_available_name(self, name, max_length=None):
    self.delete(name)
    return name 

class IndexView(base.View):
  def get(self, request):
    if 'context' in request.session and request:
      context = request.session['context']
      try:
        del request.session['context']
      except KeyError:
        pass
      return render(request, 'index.html', context)
    else:
      context = {
        "message": "No Image Selected!"
      }
      return render(request, 'index.html', context)

  def post(self, request):
    fs = CustomFileSystemStorage()
    model = load_model('app/CNN/model/cifar_model.h5')
    class_list = ["Airplane", "Automobile", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck", "Unknown"]
    
    try:
      # Casting the image to the correct datatype to fit the model.
      raw_image = request.FILES["image"]
      if not raw_image.content_type.startswith('image'):
        context = {
          "message": "Not a supported file type. Choose a different image."
        }
        request.session['context'] = context
        return redirect(reverse('index'))
        
      fs_image = fs.save(raw_image.name, raw_image)
      image_path = str(settings.MEDIA_ROOT) + "/" + raw_image.name
      cv2_image = cv2.imread(image_path)
      rgb_image = cv2.cvtColor(cv2_image, cv2.COLOR_BGR2RGB)
      rgb_image_from_array = Image.fromarray(rgb_image, 'RGB')
      resized_rgb_image = rgb_image_from_array.resize((32, 32))
      test_image =np.expand_dims(resized_rgb_image, axis=0)

      result_raw = model(test_image, training=False)
      result_list = result_raw.numpy().tolist()[0]
      result_refined = [x*100 for x in result_list]

      i = np.argmax(result_refined)
      percentage = round(result_refined[i])

      if percentage > 60:
        predicted = True
      else:
        predicted = False
        i = len(class_list) - 1

      context = {
        "filename": fs_image,
        "percentage": percentage,
        "category": class_list[i],
        "predicted": predicted,
      }
      request.session['context'] = context     
      return redirect(reverse('index'))
    
    except Exception as e:
      logger.error(e)
      return HttpResponseServerError()

class ResetView(base.View):
  def get(self, request):
    [f.unlink() for f in Path(str(settings.MEDIA_ROOT) + "/").glob("*") if f.is_file()]
    return redirect(reverse('index'))

index = IndexView.as_view()
reset_view = ResetView.as_view()
