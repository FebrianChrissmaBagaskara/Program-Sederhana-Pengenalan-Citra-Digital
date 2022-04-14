#Febrian Chrissma Bagaskara
#F551 20 059
#kelas B

import cv2

img = cv2.imread("dog.png", 0)

img_1 = 255 - img

cv2.imshow("Original Image", img)
cv2.imshow("Image Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
