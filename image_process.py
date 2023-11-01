from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
from predict import predictans

def proc(*args):
    im = Image.open("NeuraScribe/screenshot.jpg").convert("L")
    im1 = im.crop((85, 350, 315, 580))
    im1=im1.resize((28,28))
    #plt.imshow(im1,cmap='gray')
    #plt.show()
    arr=np.array(im1.getdata()).reshape(28,28)
    num=predictans(arr)
    #print("Num in proc func",num)

    return num
    
