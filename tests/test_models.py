from django.test import TestCase
from ai.model import create_cifar_model
from keras.optimizers import SGD
import numpy as np


class YourModelTestCase(TestCase):
    def setUp(self):
        # Set up any necessary data for the tests
        self.model = create_cifar_model(
            num_classes=10,
            input_shape=(32, 32, 3),
            optimizer=SGD(lr=0.001, momentum=0.9),
        )

    def test_model_structure(self):
        # Test the structure of the model
        self.assertEqual(len(self.model.layers), 16)
        self.assertEqual(self.model.layers[0].input_shape, (None, 32, 32, 3))
        self.assertEqual(self.model.layers[-1].output_shape, (None, 10))

    def test_model_training(self):
        # Test the training process of the model
        trainX = np.random.rand(100, 32, 32, 3)
        trainY = np.random.randint(10, size=(100, 10))
        history = self.model.fit(trainX, trainY, epochs=1, batch_size=10)
        self.assertIn("loss", history.history)
        self.assertIn("accuracy", history.history)
