import cv2
import matplotlib.pyplot as plt
import numpy as np
import sklearn

img = cv2.imread('Data1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
Z = np.float32(img.reshape((-1,3)))

img = cv2.pyrMeanShiftFiltering(img, 20, 30, 2)
img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)

plt.imshow(img)
plt.show()
