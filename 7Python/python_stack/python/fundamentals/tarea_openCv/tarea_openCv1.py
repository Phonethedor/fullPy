import cv2
#añado el archivo cascade para caras frontales
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# asigno la direccion y leo las imagenes
img1 = cv2.imread('1.jpg')
img2 = cv2.imread('2.jpeg')
# Lo convierto a escala de gris
gris1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gris2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
caras1 = faceCascade.detectMultiScale(gris1, 1.1, 2,)
caras2 = faceCascade.detectMultiScale(gris2, 1.1, 2,)
#añado rectangulo verde
for (x, y, w, h) in caras1:
    cv2.rectangle(img1, (x,y), (x+w, y+h), (0, 255, 0), 2)
for (x, y, w, h) in caras2:
    cv2.rectangle(img2, (x,y), (x+w, y+h), (0, 255, 0), 2)
#muestro el resultado
cv2.imshow('img', img1)
cv2.waitKey()
cv2.imshow('img', img2)
cv2.waitKey()