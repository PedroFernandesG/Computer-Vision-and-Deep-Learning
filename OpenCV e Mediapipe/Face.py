import cv2 as cv
import mediapipe as mp

# Inicializando o OpenCV
webcam = cv.VideoCapture(0)

# Inicialização Mediapipe
# Solução de reconhecimento de face
solucao = mp.solutions.face_detection
# Inicialização
reconhecedor_facial = solucao.FaceDetection()
# Desenho
desenho_rosto = mp.solutions.drawing_utils

while True:
    # Armazena o status e o frame nas respectivas variáveis
    status, frame = webcam.read()
    if not status:
        break

    # Converte a imagem de BGR para RGB
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Processa o frame para reconhecimento facial
    resultado = reconhecedor_facial.process(frame_rgb)

    # Se existir algum rosto dentro do vetor de detecções
    if resultado.detections:
        for rosto in resultado.detections:
            desenho_rosto.draw_detection(frame, rosto)

    # Mostra a tela com o frame que está capturando
    cv.imshow("Minha Tela", frame)

    # Delay de 5 milissegundos e armazena a informação se alguma tecla foi apertada
    chave = cv.waitKey(5)

    # Verificação se a tecla 'ESC' (código 27) foi pressionada para sair
    if chave == 27:
        break

# Fecha a conexão da webcam
webcam.release()
# Destroi as janelas de webcam
cv.destroyAllWindows()
