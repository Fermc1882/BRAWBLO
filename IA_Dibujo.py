import cv2
import numpy as np

# Cargar una imagen de dibujo
imagen = cv2.imread('dibujo.png', cv2.IMREAD_GRAYSCALE)

# Aplicar un umbral para convertir la imagen en blanco y negro
_, umbral = cv2.threshold(imagen, 128, 255, cv2.THRESH_BINARY)

# Encontrar contornos en la imagen umbral
contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos encontrados en la imagen original
imagen_contornos = imagen.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar las imágenes
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Contornos', imagen_contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()