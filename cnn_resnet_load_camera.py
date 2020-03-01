# -*- coding: utf-8 -*-
"""cnn_resnet_load_camera.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v9aA4LGuP-b09YWdfEHJ60y8BWcZ3u8K
"""

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
import keras
from tensorflow.keras.applications import resnet50
import urllib.request
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt

print(tf.__version__)

# Recreate the exact same model, including its weights and the optimizer
resnet50_model = tf.keras.models.load_model("/home/ninja/synopsys/models/cnn_resnet50/resnet_model.h5")

resnet50_model.build((None, 224, 224, 3))

# Show the model architecture
resnet50_model.summary()

# image loader
def get_cropped_image(img, resize=400):
  """
  resizes, and returns it
  """
  img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_CUBIC)
  return img

res = {}
lbl = ['alfoil', 'box', 'cbcontainer', 'cokecan', 'glassbottle', 'm_and_m', 'milkcan', 'plasticbottle', 'spoon', 'steelspoon', 'straw']

# Commented out IPython magic to ensure Python compatibility.
import cv2

# gstreamer_pipeline returns a GStreamer pipeline for capturing from the CSI camera
# Defaults to 1280x720 @ 60fps
# Flip the image by setting the flip_method (most common values: 0 and 2)
# display_width and display_height determine the size of the window on the screen

def gstreamer_pipeline(
    capture_width=2000,
    capture_height=2000,
    display_width=640,
    display_height=640,
    framerate=15,
    flip_method=0,
):
    return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )

lbl = ['alfoil', 'box', 'cbcontainer', 'cokecan', 'glassbottle', 'm_and_m', 'milkcan', 'plasticbottle', 'spoon', 'steelspoon', 'straw']
cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=0), cv2.CAP_GSTREAMER)

def get_image():
    if cap.isOpened():
        window_handle = cv2.namedWindow("CSI Camera", cv2.WINDOW_AUTOSIZE)
        # Window
        print("Press ESC key when ready")
        while cv2.getWindowProperty("CSI Camera", 0) >= 0:
            ret_val, img = cap.read()
            cv2.imshow("CSI Camera", img)
            if cv2.waitKey(1) & 0xFF == 27:
                return img
    else:
        print("Unable to open camera")

for x in range(5):
    img = get_image()

    cropped_img = get_cropped_image(img)
    plt.imshow(cropped_img)
    plt.show(block=False)
    plt.pause(3)
    plt.close()

    # convert the PIL image to a numpy array
    # IN PIL - image is in (width, height, channel)
    # In Numpy - image is in (height, width, channel)a
    numpy_image = img_to_array(cropped_img)
    plt.imshow(np.uint8(numpy_image))
 
    # Convert the image / images into batch format
    # expand_dims will add an extra dimension to the data at a particular axis
    # We want the input matrix to the network to be of the form (batchsize, height, width, channels)
    # Thus we add the extra dimension to the axis 0.
    image_batch = np.expand_dims(numpy_image, axis=0)
    plt.imshow(np.uint8(image_batch[0]))

    # prepare the image for the inception_v3 model
    processed_image = resnet50.preprocess_input(image_batch.copy())
 
    # get the predicted probabilities for each class
    predictions = resnet50_model.predict(processed_image)
    lst = list(zip(predictions[0], lbl))
    from operator import itemgetter
    mx = max(lst, key = itemgetter(0))
    predicted_cls = mx[1]
    print("Predicted image class = " + predicted_cls)

cap.release()
cv2.destroyAllWindows()
