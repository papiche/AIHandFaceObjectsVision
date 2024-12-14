#!/bin/env python3
import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf
import pyttsx3
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import json
import RPi.GPIO as GPIO
from time import sleep
import threading

# Configuration du Camera Tilt Hat
pan_pin = 17
tilt_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pan_pin, GPIO.OUT)
GPIO.setup(tilt_pin, GPIO.OUT)
pan = GPIO.PWM(pan_pin, 50)
tilt = GPIO.PWM(tilt_pin, 50)
pan.start(7.5)
tilt.start(7.5)

# Initialisation des modules de détection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Synthèse vocale
engine = pyttsx3.init()

# Modèles d'apprentissage profond
hand_model = tf.keras.models.load_model("hand_recognition_model.h5")
face_model = tf.keras.models.load_model("face_recognition_model.h5")

# Dictionnaire pour les utilisateurs
users = {
    "hands": {},
    "faces": {}
}

# Fonction pour ajuster la caméra
def adjust_camera(x, y):
    pan_angle = np.interp(x, [0, 1], [2.5, 12.5])
    tilt_angle = np.interp(y, [0, 1], [2.5, 12.5])
    pan.ChangeDutyCycle(pan_angle)
    tilt.ChangeDutyCycle(tilt_angle)
    sleep(0.1)

# Chargement et sauvegarde des utilisateurs
def load_users():
    if os.path.exists("users.json"):
        with open("users.json", "r") as f:
            return json.load(f)
    return {"hands": {}, "faces": {}}

def save_users():
    with open("users.json", "w") as f:
        json.dump(users, f)
    messagebox.showinfo("Succès", "Les utilisateurs ont été sauvegardés avec succès !")

# Détection et enregistrement des mains
def detect_and_register_hand():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erreur", "Impossible d'accéder à la caméra.")
        return
    messagebox.showinfo("Instruction", "Placez votre main devant la caméra et appuyez sur ESPACE pour enregistrer.")
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Échec de lecture vidéo.")
            continue
        
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                
                # Ajuster la caméra
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                adjust_camera(wrist.x, wrist.y)
                
                # Convertir les points en tableau pour le modèle d'IA
                hand_features = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
                
                # Prédiction avec le modèle d'IA
                predicted_hand = hand_model.predict(np.expand_dims(hand_features, axis=0))[0]
                recognized_hand = np.argmax(predicted_hand)
                
                # Enregistrer la main
                if cv2.waitKey(1) & 0xFF == ord(" "):
                    name = hand_name.get()
                    users["hands"][name] = recognized_hand
                    messagebox.showinfo("Succès", f"Main enregistrée sous le nom '{name}'.")
                    save_users()
                    break
        
        cv2.imshow("Détection des mains", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC pour quitter
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Détection et enregistrement des visages
def detect_and_register_face():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erreur", "Impossible d'accéder à la caméra.")
        return
    messagebox.showinfo("Instruction", "Placez votre visage devant la caméra et appuyez sur ESPACE pour enregistrer.")
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Échec de lecture vidéo.")
            continue
        
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_detection.process(image_rgb)
        
        if results.detections:
            for detection in results.detections:
                mp.solutions.drawing_utils.draw_detection(image, detection)
                
                # Ajuster la caméra
                bboxC = detection.location_data.relative_bounding_box
                adjust_camera(bboxC.xmin + bboxC.width/2, bboxC.ymin + bboxC.height/2)
                
                # Extraire les caractéristiques faciales pour le modèle d'IA
                face_image = image[int(bboxC.ymin*image.shape[0]):int((bboxC.ymin+bboxC.height)*image.shape[0]),
                                   int(bboxC.xmin*image.shape[1]):int((bboxC.xmin+bboxC.width)*image.shape[1])]
                face_image = cv2.resize(face_image, (224, 224))
                face_features = face_model.predict(np.expand_dims(face_image, axis=0))[0]
                
                # Enregistrer le visage
                if cv2.waitKey(1) & 0xFF == ord(" "):
                    name = face_name.get()
                    users["faces"][name] = face_features.tolist()
                    messagebox.showinfo("Succès", f"Visage enregistré sous le nom '{name}'.")
                    save_users()
                    break
        
        cv2.imshow("Détection des visages", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC pour quitter
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Mode de détection et prédiction
def detect_and_predict():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        messagebox.showerror("Erreur", "Impossible d'accéder à la caméra.")
        return
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Échec de lecture vidéo.")
            continue
        
        image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Détection des mains
        if hand_detection_var.get():
            hand_results = hands.process(image_rgb)
            if hand_results.multi_hand_landmarks:
                for hand_landmarks in hand_results.multi_hand_landmarks:
                    mp.solutions.drawing_utils.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    
                    hand_features = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]).flatten()
                    predicted_hand = hand_model.predict(np.expand_dims(hand_features, axis=0))[0]
                    recognized_hand = np.argmax(predicted_hand)
                    
                    for name, hand_id in users["hands"].items():
                        if hand_id == recognized_hand:
                            cv2.putText(image, f"Main: {name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            engine.say(f"Main détectée : {name}")
                            engine.runAndWait()
                            break
        
        # Détection des visages
        if face_detection_var.get():
            face_results = face_detection.process(image_rgb)
            if face_results.detections:
                for detection in face_results.detections:
                    mp.solutions.drawing_utils.draw_detection(image, detection)
                    
                    bboxC = detection.location_data.relative_bounding_box
                    face_image = image[int(bboxC.ymin*image.shape[0]):int((bboxC.ymin+bboxC.height)*image.shape[0]),
                                       int(bboxC.xmin*image.shape[1]):int((bboxC.xmin+bboxC.width)*image.shape[1])]
                    face_image = cv2.resize(face_image, (224, 224))
                    face_features = face_model.predict(np.expand_dims(face_image, axis=0))[0]
                    
                    min_distance = float('inf')
                    recognized_name = None
                    for name, stored_features in users["faces"].items():
                        distance = np.linalg.norm(np.array(stored_features) - face_features)
                        if distance < min_distance:
                            min_distance = distance
                            recognized_name = name
                    
                    if recognized_name and min_distance < 0.6:  # Seuil de similarité
                        cv2.putText(image, f"Visage: {recognized_name}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        engine.say(f"Visage détecté : {recognized_name}")
                        engine.runAndWait()
        
        if resolution_var.get():
            image = cv2.resize(image, (320, 240))
        
        cv2.imshow("Détection et Prédiction", image)
        if cv2.waitKey(5) & 0xFF == 27:  # ESC pour quitter
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Interface graphique
root = tk.Tk()
root.title("Reconnaissance des mains et visages")

hand_name = tk.StringVar()
face_name = tk.StringVar()

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Nom pour la main :").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=hand_name).grid(row=0, column=1, padx=5, pady=5)
tk.Button(frame, text="Enregistrer une main", command=detect_and_register_hand).grid(row=1, column=0, columnspan=2, pady=10)

tk.Label(frame, text="Nom pour le visage :").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(frame, textvariable=face_name).grid(row=2, column=1, padx=5, pady=5)
tk.Button(frame, text="Enregistrer un visage", command=detect_and_register_face).grid(row=3, column=0, columnspan=2, pady=10)

face_detection_var = tk.BooleanVar()
hand_detection_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Détection de visage", variable=face_detection_var).grid(row=4, column=0)
tk.Checkbutton(frame, text="Détection de main", variable=hand_detection_var).grid(row=4, column=1)

resolution_var = tk.BooleanVar()
tk.Checkbutton(frame, text="Basse résolution", variable=resolution_var).grid(row=5, column=0, columnspan=2)

hand_count = tk.IntVar(value=2)
tk.Radiobutton(frame, text="Une main", variable=hand_count, value=1).grid(row=6, column=0)
tk.Radiobutton(frame, text="Deux mains", variable=hand_count, value=2).grid(row=6, column=1)

tk.Button(frame, text="Mode Détection et Prédiction", command=detect_and_predict).grid(row=7, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Sauvegarder les utilisateurs", command=save_users).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(frame, text="Quitter", command=root.quit).grid(row=9, column=0, columnspan=2, pady=10)

# Chargement des utilisateurs existants
users = load_users()

# Traitement asynchrone
def process_frame(frame):
    # Traitement de l'image ici
    pass

def capture_and_process():
    while running:
        ret, frame = cap.read()
        if ret:
            if resolution_var.get():
                frame = cv2.resize(frame, (320, 240))
            threading.Thread(target=process_frame, args=(frame,)).start()

running = True
threading.Thread(target=capture_and_process).start()

root.mainloop()

# Nettoyage
GPIO.cleanup()
