# Como Controlar WebCam Com Python
# Introdução ao OpenCV
# Biblioteca de Visão Computacional

import cv2 as cv
#Isso permite a conexão com a webcam com o nosso computador
webcam = cv.VideoCapture(0)

#Verificando se a conexão esta correta
if webcam.isOpened():
    #Armazena o status da comunicação em Status(True or False)
    #Armazena cada frame da webcam em Frame
    Status, Frame = webcam.read()
    #Enquanto status -> True
    while Status:
        Status, Frame = webcam.read()
        #Mostra a tela com cada frame que ele esta capturando
        cv.imshow("Minha Tela",Frame)
        #Delay de 5 milisegundos e armazena a informação se alguma tecla tive sido apertada
        chave = cv.waitKey(5)

        #27 Representa a tecla ESC
        if chave == 27:
            break

    #Tira uma foto do ultimo frame quando for apertado ESC
    cv.imwrite("Foto CV.png",Frame)

#Fecha a conexão da webcam
webcam.release()
#Destroi as janelas de webcam
cv.destroyAllWindows()
