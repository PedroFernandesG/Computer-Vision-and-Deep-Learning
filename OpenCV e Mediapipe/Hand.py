import cv2 as cv
import mediapipe as mp

# Inicializando o OpenCV
webcam = cv.VideoCapture(0)

# Inicialização Mediapipe
# Solução de reconhecimento de face
solucao = mp.solutions.hands
# Inicialização
reconhecedor_hand = solucao.Hands()
# Desenho
desenho_hand = mp.solutions.drawing_utils

while True:
    # Armazena o status e o frame nas respectivas variáveis
    status, frame = webcam.read()
    if not status:
        break

    # Converte a imagem de BGR para RGB
    frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    # Processa o frame para reconhecimento facial
    resultado = reconhecedor_hand.process(frame_rgb)

    # Se existir algum rosto dentro do vetor de detecções
    if resultado.multi_hand_landmarks:
        # Escreve "S" como primeiro caractere em um arquivo
        with open("C:\\Users\\dados2.txt", 'w') as arquivo:
            arquivo.write('S')

        for hand in resultado.multi_hand_landmarks:
            desenho_hand.draw_landmarks(frame,hand,solucao.HAND_CONNECTIONS)

    else:
        with open("C:\\Users\\dados2.txt", 'w') as arquivo:
            arquivo.write('N')
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

