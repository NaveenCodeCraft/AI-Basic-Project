import cv2
import pytesseract

# Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image file
image = cv2.imread('car2.png')
#cv2.imshow("Original", image)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale", gray_image)

# Apply Canny edge detection
canny_edge = cv2.Canny(gray_image, 170, 200)
#cv2.imshow("Canny Edge Detection", canny_edge)

# Find contours based on edges
contours, _ = cv2.findContours(canny_edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]

# Initialize number plate contour and x, y, w, h coordinates
contour_with_license_plate = None
x, y, w, h = None, None, None, None

# Draw contours on a copy of the image
contours_image = image.copy()
cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)
#cv2.imshow("Image with Contours", contours_image)

# Find the contour with 4 corners
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
    if len(approx) == 4:
        contour_with_license_plate = approx
        x, y, w, h = cv2.boundingRect(contour)
        Number_plate = gray_image[y:y+h, x:x+w]
        break

# Check if number plate contour is detected
if contour_with_license_plate is not None:
    # Apply thresholding and noise reduction
    _, Number_plate = cv2.threshold(Number_plate, 127, 255, cv2.THRESH_BINARY)
    Number_plate = cv2.bilateralFilter(Number_plate, 11, 17, 17)
    cv2.imshow('Extracted Number Plate', Number_plate)

    # OCR to extract text
    text = pytesseract.image_to_string(Number_plate, config='--psm 8')
    print("Detected Number Plate Text:", text)

    # Draw the rectangle and detected text on the original image
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    #cv2.imshow("Detected Number Plate on Image", image)
else:
    print("Number plate not detected.")

cv2.waitKey(0)
cv2.destroyAllWindows()
