import cv2

img=cv2.imread("1688698757968.jpg") #read an image

cv2.imshow('Harri Potter',img) # to display the image

cv2.imwrite('photo.png',img) # to save the image with another format

cv2.waitkey(1000)

cv2.destroyAllWindows()




