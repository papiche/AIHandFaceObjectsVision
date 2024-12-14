# Système de Reconnaissance de Gestes et d'Identités

## Introduction

Ce projet combine la reconnaissance de gestes de la main et l'identification de personnes, offrant des solutions potentiellement transformatrices pour diverses applications, notamment pour la communication des personnes sourdes et malentendantes, ainsi que pour la sécurité domestique. Il repose sur des technologies de pointe telles que la vision par ordinateur, l'apprentissage profond et des dispositifs matériels comme le Hat de caméra Tilt Pan.

## Composantes Clés

1.  **Reconnaissance de Gestes de la Main :**
    *   Utilise la bibliothèque MediaPipe pour détecter et suivre les mains en temps réel.
    *   Permet l'enregistrement de gestes personnalisés, où l'utilisateur définit un geste et son étiquette associée.
    *   La reconnaissance se fait en comparant les coordonnées 3D des points de repère du geste actuel avec les gestes enregistrés.
2.  **Identification de Personnes :**
    *   Utilise un modèle d'apprentissage profond entraîné pour reconnaître les visages.
    *   Capture et enregistre les caractéristiques uniques de chaque visage, associées à un nom.
    *   En mode de détection, compare le visage détecté avec la base de données des visages enregistrés pour l'identification.
3.  **Suivi Visuel et Ajustement de la Caméra (Hat de Caméra Tilt Pan) :**
    *   Le Hat de caméra Tilt Pan permet de suivre les mouvements de la main (pour les gestes) ou du visage (pour l'identification), en ajustant dynamiquement la position de la caméra.
    *   Cette fonctionnalité assure que la main ou le visage est toujours au centre du champ de vision, améliorant ainsi la précision de la reconnaissance.
4.  **Interfaces Utilisateurs :**
    *   Une interface en ligne de commande (CLI) pour la configuration et l'enregistrement des gestes dans la deuxième version du code.
    *   Une interface utilisateur graphique (GUI) pour la première version du code, pour l'enregistrement et le contrôle de la reconnaissance de mains et de visages.
5. **Synthèse vocale**
    * Une option pour une synthèse vocale a été ajoutée dans la première version du code. Cela permet de donner des informations vocal sur les mains et les visages détectés.

## Avantages pour les Personnes Sourdes et Malentendantes

*   **Communication Améliorée :** Le système de reconnaissance de gestes de la main pourrait être utilisé comme une interface alternative pour la communication, où les gestes sont traduits en texte ou en parole, facilitant l'interaction avec les personnes non familiarisées avec la langue des signes.
*   **Apprentissage de la Langue des Signes :** Les utilisateurs pourraient utiliser le système pour pratiquer et affiner leur maîtrise de la langue des signes, en recevant un retour immédiat sur la précision de leurs gestes.
*   **Accessibilité accrue :** Pour des interactions quotidiennes, comme interagir avec des systèmes qui ne supportent pas directement la langue des signes, ou des systèmes de traduction en temps réel.
*   **Rendre l'apprentissage de la langue des signes plus amusant :** En proposant des défis et un apprentissage ludique.

## Avantages pour la Reconnaissance des Personnes (Sécurité Domestique)

*   **Surveillance Sécurisée :** Le système permet d'identifier les personnes se présentant devant votre domicile, en comparant les visages détectés avec une base de données enregistrée.
*   **Alertes Personnalisées :** Le système peut générer des alertes (sonores ou visuelles) ou des notifications en fonction de l'identité de la personne détectée. Par exemple, une notification pour l'arrivée d'un membre de la famille et un avertissement pour les personnes inconnues.
*   **Contrôle d'Accès :** Combiné avec un système de verrouillage, ce projet pourrait permettre l'accès automatisé aux personnes autorisées, en se basant sur la reconnaissance faciale.
*   **Système de surveillance simple et peu coûteux :** Le projet peut être facilement mise en place, en ne demandant que du code et le matériel nécessaire.

## Fonctionnalités Spécifiques

*   **Ajustement de la Caméra:** Le Hat de caméra Tilt Pan permet de suivre les mouvements de l'utilisateur pour toujours avoir une bonne capture d'image.
*   **Enregistrement des Gestes et des Visages :** L'utilisateur peut facilement enregistrer de nouveaux gestes et visages directement à partir de l'application.
*   **Personnalisation :** La possibilité d'ajouter, modifier ou supprimer des gestes et des visages enregistrés pour s'adapter à des besoins spécifiques.
*   **Polyvalence :** Le code peut être adapté pour être utilisé avec d'autres systèmes ou applications.

## Limites

*   **Précision :** La précision dépend de la qualité de l'image, de l'éclairage, de la variation des gestes, et de la qualité du modèle d'apprentissage profond (pour l'identification de personnes).
*   **Matériel :** Le projet nécessite un matériel spécifique comme une caméra et le Hat de caméra Tilt Pan, qui pourraient ne pas être accessibles à tous.


Ce projet de reconnaissance de gestes et d'identification de personnes est une initiative prometteuse qui peut avoir un impact significatif sur la vie des personnes sourdes et malentendantes, ainsi que sur la sécurité domestique. En tirant parti de la technologie de vision par ordinateur et de l'apprentissage profond, il offre des solutions pratiques et innovantes pour la communication et la surveillance, en faisant un outil pertinent pour une variété d'applications quotidiennes.

### Contribution

Les contributions sont les bienvenues. Veuillez ouvrir une issue ou une pull request.

### Licence

Ce projet est sous licence AGPL.

## Comparaison avec le script `enhanced_gesture_recognition.py`

Voici les principales différences entre les deux scripts :

| Caractéristique           | `enhanced_gesture_recognition.py`                               | `hand_recognition.py`                          |
| ------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------- |
| **Objectif principal**    | Reconnaissance de mains et visages.                              | Reconnaissance de gestes de la main.                            |
| **Types de détection**    | Mains et visages.                                               | Uniquement les mains.                                          |
| **Modèles d'IA**          | Utilisation de modèles d'apprentissage profond pour la reconnaissance. | Pas de modèles d'apprentissage profond pour la reconnaissance. |
| **Méthode de reconnaissance** | Basée sur la prédiction du modèle.                             | Basée sur la comparaison directe des coordonnées 3D des points de repère de la main en utilisant la distance euclidienne.     |
| **Interface utilisateur** | Interface graphique (GUI).                                         | Interface en ligne de commande.                               |
| **Gestion des données**   | Enregistrement et chargement d'informations pour les mains et visages avec le noms dans un dictionnaire.    |  Enregistrement et chargement d'informations pour les gestes avec les noms dans un dictionnaire.  |
| **Synthèse vocale**      |  Synthèse vocale.                                                 | Pas de synthèse vocale.                                          |
| **Mode de fonctionnement**    | Plusieurs options, interface visuelle.                            | Principalement axé sur l'enregistrement et la reconnaissance de gestes, via une interface textuelle.                 |
| **Traitement asynchrone**| Traitement asynchrone de l'image. | Pas de traitement asynchrone. |

**En résumé :**

*   `enhanced_gesture_recognition.py` est plus complexe et est conçu pour une reconnaissance plus sophistiquée des mains et des visages à l'aide de modèles d'apprentissage profond et d'une interface graphique.
*   `hand_recognition.py` est plus simple, se concentre sur la reconnaissance de gestes, utilise une approche de comparaison de distances plus basique et une interface en ligne de commande.

Le choix entre les deux scripts dépend de votre cas d'utilisation. Si vous avez besoin d'une reconnaissance plus précise et sophistiquée de mains et visages avec une interface utilisateur graphique, utilisez le premier script. Si votre besoin principal est la reconnaissance de gestes simples avec une interface de ligne de commande et que vous souhaitez éviter l'utilisation de modèles d'apprentissage profond, le second script est plus approprié.


---

# README pour `hand_recognition.py`

### Description

Ce script Python permet de capturer, enregistrer et reconnaître des gestes de la main en temps réel en utilisant la bibliothèque MediaPipe pour la détection des mains et un Hat de caméra Tilt Pan pour suivre la position de la main. L'application permet aux utilisateurs d'enregistrer de nouveaux gestes, d'afficher les gestes enregistrés, de reconnaître des gestes en temps réel, et de sauvegarder la base de données de gestes dans un fichier JSON.

### Fonctionnalités

*   **Détection de la main en temps réel :** Utilise MediaPipe pour détecter les mains dans le flux vidéo en direct.
*   **Suivi de la main avec le Hat de caméra Tilt Pan :** Ajuste les angles du Hat de caméra Tilt Pan pour maintenir la main détectée au centre du champ de vision.
*   **Capture de gestes :** Permet à l'utilisateur d'enregistrer un geste en appuyant sur la barre d'espace, où les coordonnées 3D des points de repère de la main sont capturées.
*   **Enregistrement des gestes :** Les gestes capturés sont stockés dans un dictionnaire, où chaque geste est associé à une étiquette définie par l'utilisateur.
*   **Chargement et sauvegarde des gestes :** La base de données de gestes peut être chargée à partir d'un fichier JSON et sauvegardée.
*   **Reconnaissance des gestes :** Compare le geste actuel avec les gestes enregistrés en utilisant la distance euclidienne, et affiche l'étiquette du geste reconnu en temps réel sur la vidéo.
*   **Interface en ligne de commande :** Utilise une interface simple en ligne de commande pour naviguer dans les différentes options de l'application.

### Prérequis

*   Python 3.6 ou une version ultérieure
*   Les bibliothèques Python suivantes :
    *   `cv2` (OpenCV)
    *   `mediapipe`
    *   `numpy`
    *   `RPi.GPIO` (nécessaire uniquement pour le contrôle du Hat de caméra Tilt Pan)
*   Un Hat de caméra Tilt Pan (nécessaire pour le suivi de la main)
*   Une caméra

### Installation

1.  Clonez le dépôt :

    ```
    git clone <le lien vers le dépôt>
    cd <nom du dépôt>
    ```

2.  Installez les bibliothèques Python nécessaires :

    ```
    pip install opencv-python mediapipe numpy
    ```

    Installez également `RPi.GPIO` pour Raspberry Pi :

    ```
    pip install RPi.GPIO
    ```

### Comment utiliser

1.  Exécutez le script :

    ```
    python enhanced_gesture_recognition_v2.py
    ```

2.  L'application affichera un menu en ligne de commande. Choisissez une des options suivantes :
    *   `1` : Enregistrer un nouveau geste.
    *   `2` : Afficher les gestes enregistrés.
    *   `3` : Reconnaître un geste en temps réel.
    *   `4` : Sauvegarder et quitter.
3.  Pour enregistrer un geste, vous devrez entrer une étiquette (lettre, mot, ou phrase). Ensuite, placez votre main devant la caméra et appuyez sur la barre d'espace pour capturer le geste.
4.  Pour la reconnaissance de gestes en temps réel, placez votre main devant la caméra. L'étiquette du geste reconnu est affichée sur la vidéo. Appuyez sur la touche Échap pour quitter la reconnaissance.

### Notes

*   La précision de la reconnaissance des gestes dépend de la qualité de la capture des gestes et des similarités entre les différents gestes.
*   Le Hat de caméra Tilt Pan est optionnel. Si le Hat n'est pas détecté, l'application continue de fonctionner, mais sans l'ajustement de la caméra.
*   Les informations sur les gestes sont sauvegardées dans un fichier `gestures.json`.


---

# README pour `enhanced_gesture_recognition.py`

## Description

Ce projet Python combine la détection de mains et de visages en temps réel avec la reconnaissance d'entités à l'aide de modèles d'apprentissage profond pré-entraînés. Il comprend également une interface utilisateur graphique (GUI) pour une interaction facile avec les utilisateurs et une option d'ajustement de la caméra via un Hat de caméra Tilt Pan.

## Fonctionnalités

-   **Détection de main en temps réel :** Utilise MediaPipe pour détecter les mains dans le flux vidéo en direct.
-   **Reconnaissance de main :** Utilise un modèle d'apprentissage profond entraîné pour identifier les mains enregistrées.
-   **Détection de visage en temps réel :** Utilise MediaPipe pour détecter les visages dans le flux vidéo en direct.
-   **Reconnaissance de visage :** Utilise un modèle d'apprentissage profond entraîné pour identifier les visages enregistrés.
-   **Ajustement de caméra :** Contrôle un Hat de caméra Tilt Pan pour suivre les mains et les visages détectés.
-   **Synthèse vocale :** Fournit une rétroaction vocale en utilisant le module `pyttsx3` pour les mains et les visages détectés.
-   **Interface utilisateur graphique :** Fournit une interface utilisateur graphique pour enregistrer de nouvelles mains et de nouveaux visages, pour exécuter l'application et pour contrôler le mode de détection.
-   **Enregistrement et chargement des utilisateurs :** Les informations utilisateur (noms de mains et de visages enregistrés) sont sauvegardées dans un fichier JSON et chargées au démarrage de l'application.
-   **Traitement asynchrone** : Les images de la caméra sont traitées dans un thread séparé.

## Prérequis

-   Python 3.6 ou une version ultérieure
-   Les bibliothèques Python suivantes :
    -   `cv2` (OpenCV)
    -   `mediapipe`
    -   `numpy`
    -   `tensorflow`
    -   `pyttsx3`
    -   `tkinter`
    -   `RPi.GPIO` (nécessaire uniquement pour le contrôle du Hat de caméra Tilt Pan)

-   Modèles d'apprentissage profond entraînés :
    -   `hand_recognition_model.h5`
    -   `face_recognition_model.h5`
    -  (Ces modèles ne sont pas inclus dans le dépôt et doivent être fournis séparément.)

-  Un Hat de caméra Tilt Pan (nécessaire uniquement pour l'ajustement de la caméra)
-  Une caméra

## Installation

1.  Clonez le dépôt :

    ```
    git clone <le lien vers le dépôt>
    cd <le nom du dépôt>
    ```

2.  Installez les bibliothèques Python nécessaires :

    ```
    pip install opencv-python mediapipe numpy tensorflow pyttsx3 tk
    ```

    Installez également `RPi.GPIO` pour Raspberry Pi :

    ```
    pip install RPi.GPIO
    ```

3.  Assurez-vous que les modèles d'apprentissage profond entraînés (`hand_recognition_model.h5` et `face_recognition_model.h5`) sont placés dans le même répertoire que le script `enhanced_gesture_recognition.py`.

## Comment utiliser

1.  Exécutez le script :

    ```
    python enhanced_gesture_recognition.py
    ```

2.  L'interface utilisateur graphique (GUI) apparaîtra :
    -   Entrez un nom pour la main que vous souhaitez enregistrer et cliquez sur le bouton `Enregistrer une main`.
    -   Entrez un nom pour le visage que vous souhaitez enregistrer et cliquez sur le bouton `Enregistrer un visage`.
    -   Cochez la case `Détection de visage` ou `Détection de main` pour activer le mode de détection.
    -   Cochez la case `Basse résolution` pour réduire la résolution du flux vidéo.
    -   Sélectionnez `Une main` ou `Deux mains` pour changer le nombre de mains détectées.
    -   Cliquez sur le bouton `Mode Détection et Prédiction` pour démarrer la détection.
    -   Cliquez sur le bouton `Sauvegarder les utilisateurs` pour enregistrer les noms.
    -   Cliquez sur le bouton `Quitter` pour fermer l'application.

3.  Dans le mode d'enregistrement, placez votre main ou votre visage devant la caméra et appuyez sur ESPACE pour l'enregistrer.
4.  Dans le mode Détection et Prédiction, le flux vidéo avec les mains et/ou les visages détectés s'affichera. Une synthèse vocale informera des détections effectuées.
5.  Appuyez sur la touche `Échap` pour fermer l'application.

## Remarques importantes

-   La précision de la reconnaissance des mains et des visages dépend des modèles entraînés fournis.
-   Le Hat de caméra Tilt Pan est optionnel. Si le Hat n'est pas détecté, l'application continue de fonctionner, mais sans l'ajustement de la caméra.
-   Les informations utilisateur sont sauvegardées dans un fichier `users.json`.
-   Assurez-vous que votre caméra est connectée et accessible avant de lancer l'application.

## Contribution

Les contributions sont les bienvenues. Veuillez ouvrir une issue ou une pull request.

## Licence

Ce projet est sous licence AGPL.
