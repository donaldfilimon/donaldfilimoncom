import unittest
from keras.models import load_model
import numpy as np
from PIL import Image
import os

class TestAIModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model_path = 'ai/CNN/model/cifar_model.h5'
        cls.model = load_model(cls.model_path)
        cls.class_list = ["Airplane", "Automobile", "Bird", "Cat", "Deer", "Dog", "Frog", "Horse", "Ship", "Truck", "Unknown"]

    def test_model_loading(self):
        self.assertIsNotNone(self.model, "Model should be loaded successfully")

    def test_model_prediction(self):
        # Create a dummy image for testing
        dummy_image = np.random.rand(32, 32, 3) * 255
        dummy_image = Image.fromarray(dummy_image.astype('uint8')).resize((32, 32))
        test_image = np.expand_dims(dummy_image, axis=0)

        # Get prediction
        result_raw = self.model(test_image, training=False)
        result_list = result_raw.numpy().tolist()[0]
        result_refined = [x*100 for x in result_list]

        i = np.argmax(result_refined)
        percentage = round(result_refined[i])

        if percentage > 60:
            predicted = True
        else:
            predicted = False
            i = len(self.class_list) - 1

        self.assertIn(self.class_list[i], self.class_list, "Predicted class should be in the class list")
        self.assertTrue(0 <= percentage <= 100, "Prediction percentage should be between 0 and 100")

if __name__ == '__main__':
    unittest.main()
