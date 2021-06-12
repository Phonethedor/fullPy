import cv2
#importo el archivo cascade para caras frontales
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# asigno la direccion y leo las imagenes
imagen1 = r'E:\Users\alvar\Desktop\FsPython\7Python\python_stack\python\fundamentals\tarea_openCv\1.jpg'
img1 = cv2.imread(imagen1)
imagen2 = r'E:\Users\alvar\Desktop\FsPython\7Python\python_stack\python\fundamentals\tarea_openCv\2.jpeg'
img2 = cv2.imread(imagen2)
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