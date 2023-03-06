# Importar las librerías necesarias
import mediapipe as mp
import pyautogui
import cv2

# Inicializar los módulos de detección y dibujo de puntos y conexiones de la mano
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Configurar la detección de manos, permitiendo detectar hasta 2 manos
# y estableciendo la confianza mínima para detectar y rastrear la mano
with mp_hands.Hands(
    max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:

    # Configurar la captura de video desde la cámara del dispositivo
    cap = cv2.VideoCapture(0)

    # Inicializar la variable que indicará si ambas manos están cerradas
    hands_closed = False

    # Iterar mientras la captura de video esté activa
    while cap.isOpened():
        # Leer un fotograma del video
        success, image = cap.read()
        if not success:
            break

       

            # Si se detectaron dos manos en el fotograma
            if len(results.multi_hand_landmarks) >= 2:
                # Obtener los puntos de referencia de la mano izquierda y derecha
                left_hand = results.multi_hand_landmarks[0].landmark
                right_hand = results.multi_hand_landmarks[1].landmark

                # Si el dedo índice de la mano izquierda está a la izquierda del dedo medio
                # y el dedo índice de la mano derecha está a la derecha del dedo medio
                if left_hand[4].x < left_hand[3].x and right_hand[4].x > right_hand[3].x:
                    # Si ambas manos no están cerradas, marcar que lo están
                    if not hands_closed:
                        hands_closed = True
                # Si no se cumple la condición anterior
                else:
                    # Si ambas manos están cerradas, hacer un clic con el mouse y marcar que no lo están
                    if hands_closed:
                        pyautogui.click()
                        hands_closed = False

        

    # Liberar los recursos de la captura de video y cerrar las ventanas abiertas
    cap.release()
    cv2.destroyAllWindows()
