import cv2
img = cv2.imread('poto.png')
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

# the rotation angle 
angle = 60

# Perform the rotation
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_img = cv2.warpAffine(img, M, (w, h))

# Display the rotated image
cv2.imshow("Rotated Image", rotated_img)
cv2.waitKey(0)
