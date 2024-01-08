from numpy.core.arrayprint import printoptions
from test1 import ImagSteg
from PIL import Image
import pandas as pd
import numpy as np
import cv2


img = ImagSteg()
#msginput=input("enter a msg")
#imagepath=input('enter the image path without ""')
#img.encrypt_text_in_image("exp1.jpg",msginput,"static/")
#img.encrypt_text_in_image("exp2.png",msginput,"static/")
'''choice=input("enter 1 to encode //// Enter 0 to decode")
if choice=="1":
    msginput=input("enter a msg")
    imagepath=input('enter the image path without ""')
    img.encrypt_text_in_image(imagepath,msginput,"static/")
elif choice=="0":
    imagepath=input('enter the image path without ""')
    res = img.decrypt_text_in_image(imagepath)
    print(res)'''

choice=input("enter 1 to encode //// Enter 0 to decode")
if choice=="1":
    msginput=input("enter a msg")
    img.encrypt_text_in_image("exp1.jpg",msginput,"static/")
    #img.encrypt_text_in_image("exp2.png",msginput,"static/")
elif choice=="0":
    res = img.decrypt_text_in_image("static/exp1_encrypted.png")
    print(res)
else:
    print("wrong input")


#img.encrypt_text_in_image(imagepath,msginput,"static/")
#res = img.decrypt_text_in_image("static/exp1_encrypted.png")
#print(res)
