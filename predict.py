import tensorflow as tf
keras=tf.keras
import numpy as np
import matplotlib.pyplot as plt

def predictans(image):
    model=keras.models.load_model('NeuraScribe/mnist.modelkivy')
    num=model.predict(image.reshape(1,28,28,1))
    num=np.argmax(num)
    #print("Num in predict func",num)
    #plt.imshow(image, cmap='gray')
    #plt.title(f"My neural network predicts {num} !")
    #plt.show()
    return num