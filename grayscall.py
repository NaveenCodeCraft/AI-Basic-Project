import cv2

img=cv2.imread(r"1688698757968.jpg") #r=raw string

grayIamge = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

'''cv2.imshow('original',img)

cv2.imshow('gray', grayIamge)

cv2.imwrite('grayNew.png',grayIamge)'''

print(img.shape)
print(img.size)


