import sys
import time
import keras
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("TKAgg")

from keras.models import load_model
from keras.optimizers import SGD
from keras.datasets import cifar10
from keras.utils import to_categorical
from model import create_cifar_model


def load_dataset():
    (trainX, trainY), (testX, testY) = cifar10.load_data()
    trainY = to_categorical(trainY)
    testY = to_categorical(testY)
    return trainX, trainY, testX, testY


def normalize_data(train, test):
    train_norm = train.astype("float32")
    test_norm = test.astype("float32")
    # normalize to range 0-1
    train_norm = train_norm / 255.0
    test_norm = test_norm / 255.0
    return train_norm, test_norm


# plot diagnostic learning curves
def summarize_diagnostics(history):
    # plot loss
    plt.subplot(211)
    plt.title("Cross Entropy Loss")
    plt.plot(history.history["loss"], color="blue", label="train")
    plt.plot(history.history["val_loss"], color="orange", label="test")
    # plot accuracy
    plt.subplot(212)
    plt.title("Classification Accuracy")
    plt.plot(history.history["accuracy"], color="blue", label="train")
    plt.plot(history.history["val_accuracy"], color="orange", label="test")
    # save plot to file
    filename = sys.argv[0].split("/")[-1]
    plt.savefig(filename + "_plot.png")
    plt.show()


epochs = 20
batch_size = 128
input_shape = (32, 32, 3)
num_classes = 10
timestamp = time.time()
callbacks = (
    keras.callbacks.ModelCheckpoint(
        f"cifar_model_{timestamp}.h5",
        monitor="val_loss",
        save_best_only=True,
        verbose=1,
    ),
)


def train():
    trainX, trainY, testX, testY = load_dataset()
    trainX, testX = normalize_data(trainX, testX)
    try:
        model = load_model("cifar_model.h5")
        print("Successfully loaded model.")
    except:
        print("Creating model")
        model = create_cifar_model(
            num_classes, input_shape, optimizer=SGD(lr=0.001, momentum=0.9)
        )
    finally:
        try:
            model.summary()
            history = model.fit(
                trainX,
                trainY,
                batch_size=batch_size,
                validation_data=(testX, testY),
                epochs=epochs,
                callbacks=callbacks,
            )
            summarize_diagnostics(history)
        except Exception as e:
            print(e)


train()
