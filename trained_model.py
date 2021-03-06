# -*- coding: utf-8 -*-
"""Model_Demo_File.ipynb
Created by Aravind R Krishnan
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1BRvmIlk4lgc-UMRxssbJtJxRk1h4bAdE
"""

#Loading the model and testing 
from keras.models import load_model
from keras.preprocessing import image 
import numpy as np
import matplotlib.pyplot as plt

model = load_model('MINI_PROJECT_MODEL_FINAL.h5')

def pred(path):
    test = image.load_img(path, target_size =(256,256))
    test = image.img_to_array(test)
    
    plt.imshow(test, cmap='gray')
    plt.show()
    
    test = np.expand_dims(test, axis=0)   
    result = model.predict(test)
    if result[0][0] == 1:
        print("CUPCAKES!")
    elif result[0][1] == 1:
        print("DUMPLINGS")
    elif result[0][2] == 1:
        print("FRENCH FRIES")
    elif result[0][3] == 1:
        print("FRIED RICE")
    else:
        print("PIZZA!")

def demo():
    flag=1
    while flag:
        print("Input File Path of Image: ")
        filepath=input()
        pred(filepath)
        print("Enter 0 to Quit, else 1")
        flag=input()

demo()
