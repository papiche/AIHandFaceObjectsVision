#!/bin/env python3
import cv2
import mediapipe as mp
import numpy as np
import json
import RPi.GPIO as GPIO
from time import sleep

# Configuration du Camera Tilt Hat
pan_pin = 17
tilt_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)

pan = GPIO.PWM(pan_pin, 50)
tilt = GPIO.PWM(tilt_pin, 50)

pan.start(7.5)  # Position neutre
tilt.start(7.5)

# Initialisation de MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Initialisation de la caméra
cap = cv2.VideoCapture(0)

# Dictionnaire pour stocker les gestes
gestures = {}

# Fonction pour ajuster la caméra en fonction des coordonnées de la main
def adjust_camera(hand_landmarks):
    x = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].x
    y = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST].y

    pan_angle = np.interp(x, [0, 1], [2.5, 12.5])  # Ajustez les valeurs selon votre configuration
    tilt_angle = np.interp(y, [0, 1], [2.5, 12.5])

    pan.ChangeDutyCycle(pan_angle)
    tilt.ChangeDutyCycle(tilt_angle)
    sleep(0.1)

# Fonction pour capturer un geste
def capture_gesture():
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignorer le cadre vide de la caméra.")
            continue

        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                adjust_camera(hand_landmarks)
                mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow('Détection des mains', image)
        key = cv2.waitKey(5)
        if key == 32:  # Barre d'espace pour capturer
            if results.multi_hand_landmarks:
                return [[lm.x, lm.y, lm.z] for lm in results.multi_hand_landmarks[0].landmark]
            else:
                print("Aucune main détectée.")
                return None
        elif key == 27:  # ESC pour quitter
            return None

# Fonction principale
def main():
    global gestures

    # Charger les gestes existants si le fichier JSON est présent
    try:
        with open('gestures.json', 'r') as f:
            gestures = json.load(f)
            print("Gestes chargés depuis gestures.json.")
    except FileNotFoundError:
        print("Aucun fichier de gestes trouvé, démarrage avec une base vide.")

    while True:
        print("\n1. Enregistrer un nouveau geste")
        print("2. Afficher les gestes enregistrés")
        print("3. Reconnaître un geste en temps réel")
        print("4. Sauvegarder et quitter")
        choice = input("Choisissez une option : ")

        if choice == '1':
            label = input("Entrez une lettre, un mot ou une phrase pour ce geste : ")
            print("Placez votre main devant la caméra et appuyez sur la barre d'espace pour capturer.")
            gesture_data = capture_gesture()
            if gesture_data:
                gestures[label] = gesture_data
                print(f"Geste pour '{label}' enregistré.")
            else:
                print("Capture annulée.")
        elif choice == '2':
            print("\nGestes enregistrés :")
            for label in gestures:
                print(f"- {label}")
        elif choice == '3':
            print("Placez votre main devant la caméra pour reconnaître un geste...")
            while True:
                success, image = cap.read()
                if not success:
                    print("Erreur avec la caméra.")
                    break

                image = cv2.flip(image, 1)
                image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                results = hands.process(image_rgb)

                if results.multi_hand_landmarks:
                    for hand_landmarks in results.multi_hand_landmarks:
                        current_gesture = [[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]

                        # Comparaison avec les gestes enregistrés
                        recognized_label = None
                        min_distance = float('inf')

                        for label, saved_gesture in gestures.items():
                            distance = np.linalg.norm(np.array(saved_gesture) - np.array(current_gesture))
                            if distance < min_distance:
                                min_distance = distance
                                recognized_label = label

                        if recognized_label:
                            print(f"Geste reconnu : {recognized_label}")
                            cv2.putText(image, f"Geste : {recognized_label}", (50, 50),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                cv2.imshow('Reconnaissance de geste', image)
                if cv2.waitKey(5) & 0xFF == 27:  # ESC pour quitter
                    break
        elif choice == '4':
            with open('gestures.json', 'w') as f:
                json.dump(gestures, f)
            print("Gestes sauvegardés. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

    cap.release()
    cv2.destr
