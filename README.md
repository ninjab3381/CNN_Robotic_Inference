# Solve America's Recycling Problem using Robotic ConvNets
Detection and classification of recyclable items to help recyclable facility robots identify and pick them up correctly

 - ## pics folder
   - includes the images of the recyclable and non-recycable objects used in training and validation of ConvNets. 
   - The images were taken using a Mac camera and the OpenCV-Python library
 
 - ## cnn_resnet_load_camera.py
   - Python main program
   - Loaded in Jetson Nano
   - Using OpenCV-Python, opens connection to camera. Takes and reads the picture
   - Load the model on the Jetson Nano kit.
   - Invoke the trained model to read the image and predict the class
   - Based on the prediction, send a signal to the Nano Microcontroller to bin the item correctly
   
 - ## cnn_resnet.ipynb, cnn_inception.ipynb, cnn_vgg.ipynb
   - Programs created using Jupyter notebook in Google Colab to create the trained ConvNet models
