#!/usr/bin/env python
# coding: utf-8

# # Image to pancil Sketch with python 

# In[ ]:


import cv2
import numpy as np

def pencil_sketch(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = cv2.bitwise_not(gray_image)
    blurred_image = cv2.GaussianBlur(inverted_gray_image, (111, 111), 0)
    inverted_blurred_image = cv2.bitwise_not(blurred_image)
    pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
    return pencil_sketch

input_image_path = "D:\mobile data\Tara singh sunny paji.jpg" #paste Image path copy jpg
output_sketch_path = 'pencil_sketch.jpg'

sketch = pencil_sketch(input_image_path)
cv2.imwrite(output_sketch_path, sketch)
cv2.imshow('Pencil Sketch', sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




