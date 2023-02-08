import cv2
import pytesseract
import numpy as np

def print_text():
    text = pytesseract.image_to_string(img)
    print(text[:-1])

def opening(image):
    kernel = np.ones((3,2),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

size = 1600

img = cv2.imread('test_ball_3.png')
img = cv2.resize(img, [size, size])
img = img[int(size/4):int(size/4*3), int(size/4):int(size/4*3)]
#img = cv2.rotate(img, cv2.ROTATE_180)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.medianBlur(img,5)
ret,img = cv2.threshold(img,70,255,cv2.THRESH_BINARY)
img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
img = opening(img)

img = cv2.Canny(img, 100, 200)


h, w = img.shape

print_text()

boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.waitKey(0)
#image = image.resize((400, 200))

