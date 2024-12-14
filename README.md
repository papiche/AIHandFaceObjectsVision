# 👋 Bienvenue dans le Projet AI Hand & Face Vision !

## L'Innovation au Bout des Doigts... et du Visage 🚀

Ce projet révolutionnaire combine la puissance de la vision par ordinateur et de l'intelligence artificielle pour vous offrir un système de reconnaissance de gestes de la main et d'identification de personnes. Imaginez les possibilités : une communication plus accessible pour tous, une sécurité renforcée pour votre domicile, et une toute nouvelle façon d'interagir avec votre environnement !

### ✨ Ce Que Vous Allez Découvrir

Ce projet, c'est un peu comme un couteau suisse pour la reconnaissance d'entités ! Il est divisé en deux versions :

1.  **`enhanced_gesture_recognition.py` : Le Maître de l'Identification Multi-Modale**
    *   Détecte et reconnaît à la fois les mains et les visages avec une précision bluffante.
    *   S'appuie sur des modèles d'apprentissage profond pour une reconnaissance de haut vol.
    *   Intègre une interface graphique (GUI) intuitive, pour un contrôle total.
    *   Vous parle grâce à la synthèse vocale, pour une expérience utilisateur immersive.
    *   S'adapte à votre environnement grâce à son Hat de Caméra Tilt Pan intégré.
2.  **`hand_recognition.py` : Le Spécialiste du Geste**
    *   Se concentre sur la capture, l'enregistrement et la reconnaissance de gestes de la main en temps réel.
    *   Utilise une approche simple et efficace de comparaison des coordonnées des points de repère de la main.
    *   Propose une interface en ligne de commande (CLI) pour une utilisation rapide et pratique.
    *   Maintient toujours la main dans le champ de vision, grâce au Hat de Caméra Tilt Pan.

## 🌟 Pourquoi Utiliser ce Projet ?

Ce projet n'est pas seulement un amas de lignes de code. C'est une porte ouverte sur un monde d'applications :

**Pour les Personnes Sourdes et Malentendantes :**

*   **Communication sans Barrières :** Transformez vos gestes en texte ou en parole, et communiquez plus facilement avec tout le monde.
*   **Apprentissage Ludique :** Pratiquez et perfectionnez votre langue des signes grâce à une rétroaction immédiate.
*   **Accessibilité Totale :** Interagissez avec des systèmes non adaptés à la langue des signes, grâce à notre système de traduction en temps réel.

**Pour la Sécurité Domestique :**

*   **Surveillance Intelligente :** Identifiez qui est à votre porte, grâce à la reconnaissance faciale.
*   **Alertes Personnalisées :** Recevez des notifications pour les membres de votre famille et soyez alerté en cas de visite inconnue.
*   **Accès Facilité :** Utilisez la reconnaissance faciale pour ouvrir votre porte aux personnes autorisées.
*   **Un système de sécurité qui peut être mis en place rapidement et facilement :** Tout le matériel et code sont facilement accessible.

## ⚙️ Fonctionnalités en Détail

*   **Vision Intelligente :** Nos algorithmes avancés détectent et suivent les mains et les visages avec une précision remarquable.
*   **Enregistrement Facile :** Enregistrez de nouveaux gestes et de nouveaux visages en un clin d'œil.
*   **Adaptation Automatique :** Notre Hat de Caméra Tilt Pan ajuste la caméra pour toujours garder l'action au centre.
*   **Personnalisation Totale :** Adaptez le projet à vos besoins, en ajoutant, modifiant ou supprimant les gestes et les visages enregistrés.
*   **Flexibilité :** Intégrez notre code à d'autres systèmes ou applications, pour une polyvalence maximale.

## 🛠️ Prérequis

Avant de commencer, assurez-vous d'avoir :

*   Python 3.6+
*   Les bibliothèques Python suivantes :
    *   `opencv-python`
    *   `mediapipe`
    *   `numpy`
    *   `tensorflow` (pour `enhanced_gesture_recognition.py`)
    *   `pyttsx3` (pour `enhanced_gesture_recognition.py`)
    *   `tkinter` (pour `enhanced_gesture_recognition.py`)
    *   `RPi.GPIO`
*   Un Hat de Caméra Tilt Pan
*   Une caméra

## 🚀 Mise en Route

1.  **Clonez le Dépôt :**

    ```bash
    git clone https://github.com/papiche/AIHandFaceObjectsVision.git
    cd AIHandFaceObjectsVision
    ```

2.  **Installez les Bibliothèques :**

    ```bash
    pip install opencv-python mediapipe numpy tensorflow pyttsx3 tk RPi.GPIO
    ```

3.  **Placez les Modèles d'Apprentissage Profond :** (uniquement pour `enhanced_gesture_recognition.py`)
    Assurez-vous que `hand_recognition_model.h5` et `face_recognition_model.h5` sont dans le même dossier que le script.

4.  **Lancez les Scripts :**
    *   Pour `enhanced_gesture_recognition.py` : `python enhanced_gesture_recognition.py`
    *   Pour `hand_recognition.py` : `python hand_recognition.py`

5.  **Suivez les Instructions :**
    *   L'interface GUI ou la CLI vous guideront pour enregistrer, détecter et reconnaître des gestes et des visages.

## 🤔 Limites (Pour Être Tout à Fait Transparent)

*   **Précision :** La précision dépend de la qualité de l'image, de l'éclairage et de la variation des gestes.
*   **Matériel :** L'utilisation du Hat de Caméra Tilt Pan améliore l'expérience, mais n'est pas obligatoire pour le fonctionnement de base du projet.
*   **Modèles IA :** L'efficacité de `enhanced_gesture_recognition.py` dépend des modèles d'IA utilisés.

## 🤝 Contribuez et Échangez

Votre contribution est la bienvenue ! N'hésitez pas à ouvrir des issues ou des pull requests pour améliorer ce projet.

## ⚖️ Licence

Ce projet est sous licence AGPL, pour une utilisation libre et ouverte à tous.

**En bref : Ce projet n'est pas qu'un simple code, c'est un outil puissant pour innover, communiquer et sécuriser !**
