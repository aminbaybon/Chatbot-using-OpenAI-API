import cv2 as cv2
import  numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('hinton.jpg')
# cv2.imshow('img' ,img)
plt.figure(figsize=(5,5))
plt.imshow(img , cmap = 'gray')
plt.axis('off')