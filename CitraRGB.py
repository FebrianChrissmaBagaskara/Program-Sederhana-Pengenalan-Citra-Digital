#Febrian Chrissma Bagaskara
#F551 20 059
#kelas B

import cv2
import numpy as np

img = cv2.imread("cat.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gambar Original", img)
cv2.imshow("Gambar GrayScale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
