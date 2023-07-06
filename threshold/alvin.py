import cv2

# membaca gambar
img = cv2.imread('elon.jpg', 255)

# menentukan threshold
thresh_value = 100

# thresholding gambar
ret, thresh = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)

# menampilkan gambar asli dan hasil thresholding
#cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh)

# menunggu tombol untuk ditutup
cv2.waitKey(0)
cv2.destroyAllWindows()
