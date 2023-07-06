import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image):
    # Mengambil nilai piksel minimum dan maksimum
    min_val = np.min(image)
    max_val = np.max(image)

    # Menyesuaikan rentang nilai piksel
    stretched_image = (image - min_val) * (255.0 / (max_val - min_val))

    return stretched_image

# Membaca gambar menggunakan matplotlib
image = plt.imread('rgb.jpg')

# Membuat salinan gambar asli
original_image = np.copy(image)

# Konversi gambar menjadi grayscale jika diperlukan
if len(image.shape) > 2:
    image = np.mean(image, axis=2)

# Melakukan contrast stretching
stretched_image = contrast_stretching(image)

# Menampilkan gambar asli dan gambar hasil contrast stretching
plt.figure(figsize=(10, 5))

# Menampilkan gambar asli
plt.subplot(1, 2, 1)
plt.imshow(original_image)
plt.title('Original Image')

# Menampilkan gambar hasil contrast stretching
plt.subplot(1, 2, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title('Contrast Stretched Image')

# Menampilkan plot
plt.tight_layout()
plt.show()

