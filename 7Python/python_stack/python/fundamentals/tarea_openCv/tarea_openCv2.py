import cv2
#añado el archivo cascade para caras frontales
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#para capturar video desde la webCam
cap = cv2.VideoCapture(0)
while True:
    #Analiza el cuadro
    _, img = cap.read()
    #lo convierto a escala de gris
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #detecta caras
    caras = face_cascade.detectMultiScale(gris, 1.1, 4)
    #añado rectangulo verde
    for (x, y, w, h) in caras:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    #muestro el resultado
    cv2.imshow('img', img)
    #se detiene si presiono escape
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break        
#fin de la captura
cap.release()