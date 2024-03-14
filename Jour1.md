# Cours Pygame

## Introduction à Pygame

Pygame est une bibliothèque de développement de jeux en Python. Elle fournit des fonctionnalités pour créer des jeux en offrant un accès facile à la gestion des graphismes, de l'audio et des entrées utilisateur.

## Installation de Pygame

Avant de commencer à utiliser Pygame, assurez-vous de l'avoir installé. Vous pouvez l'installer via pip en exécutant la commande suivante dans votre terminal :

```
pip install pygame
```

## Configuration de Pygame

Pour commencer à utiliser Pygame, vous devez importer la bibliothèque dans votre code Python. Voici comment vous pouvez le faire :

```python
import pygame
```

## Initialisation de Pygame

Avant d'utiliser les fonctionnalités de Pygame, vous devez initialiser la bibliothèque. Cela se fait en appelant `pygame.init()`.

```python
pygame.init()
```

## Création d'une fenêtre

Pour afficher votre jeu, vous devez créer une fenêtre. Utilisez la fonction `pygame.display.set_mode()` pour cela.

```python
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mon Premier Jeu Pygame")
```

## Boucle de jeu

La boucle de jeu est une boucle qui exécute continuellement votre jeu jusqu'à ce que vous décidiez de le fermer. À chaque itération de la boucle, vous pouvez mettre à jour l'état du jeu, gérer les événements et dessiner les éléments de jeu sur l'écran.

```python
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Code de mise à jour du jeu

    # Code de dessin sur l'écran

    pygame.display.update()

pygame.quit()
```


## Gestion des événements dans Pygame

Dans Pygame, les événements sont utilisés pour détecter les interactions de l'utilisateur avec le jeu, telles que les clics de souris, les touches du clavier, etc. La boucle principale de votre jeu est responsable de la gestion des événements en parcourant la file d'attente d'événements et en réagissant en conséquence.

### La boucle de gestion des événements

Dans la boucle principale de votre jeu, vous utilisez `pygame.event.get()` pour récupérer tous les événements survenus depuis la dernière itération de la boucle. Ensuite, vous parcourez cette liste d'événements et répondez à chaque événement en fonction de son type.

Voici comment cela fonctionne en pratique :

```python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        # Gérer les événements de pression de touche
    elif event.type == pygame.KEYUP:
        # Gérer les événements de relâchement de touche
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Gérer les événements de clic de souris
    elif event.type == pygame.MOUSEBUTTONUP:
        # Gérer les événements de relâchement de clic de souris
    # Ajoutez d'autres types d'événements selon les besoins de votre jeu
```

### Principaux types d'événements

#### `pygame.QUIT`

Cet événement est déclenché lorsque l'utilisateur clique sur le bouton de fermeture de la fenêtre. Vous pouvez utiliser cela pour arrêter proprement votre jeu.

#### `pygame.KEYDOWN` et `pygame.KEYUP`

Ces événements sont déclenchés lorsque l'utilisateur appuie sur une touche du clavier (`KEYDOWN`) ou la relâche (`KEYUP`). Vous pouvez les utiliser pour détecter les actions du joueur telles que la saisie de texte, le déplacement d'un personnage, etc.

#### `pygame.MOUSEBUTTONDOWN` et `pygame.MOUSEBUTTONUP`

Ces événements sont déclenchés lorsque l'utilisateur clique sur un bouton de la souris (`MOUSEBUTTONDOWN`) ou le relâche (`MOUSEBUTTONUP`). Vous pouvez les utiliser pour détecter les clics de souris, par exemple pour sélectionner des éléments dans le jeu.

### Autres types d'événements

Pygame prend également en charge d'autres types d'événements, tels que les événements de joystick, de fenêtre, etc. Vous pouvez les utiliser en fonction des besoins spécifiques de votre jeu.

### Conclusion

La gestion des événements est une partie essentielle de la création de jeux avec Pygame. En comprenant comment détecter et réagir aux événements, vous pouvez créer des interactions utilisateur fluides et captivantes dans votre jeu. N'hésitez pas à expérimenter avec différents types d'événements pour répondre aux besoins spécifiques de votre jeu.

## Dessin sur l'écran

Pygame offre de nombreuses fonctions pour dessiner des formes, des images et du texte sur l'écran. Cela vous permet de créer des éléments visuels pour votre jeu et de les mettre à jour en fonction de l'état du jeu.

### Dessin de formes géométriques

Pygame fournit des fonctions simples pour dessiner des formes géométriques telles que des rectangles, des cercles et des lignes. Vous pouvez utiliser ces fonctions pour créer des éléments tels que des décors, des interfaces utilisateur et des effets visuels.

Voici quelques exemples :

#### Dessin d'un rectangle :

```python
pygame.draw.rect(screen, color, rect)
```

#### Dessin d'un cercle :

```python
pygame.draw.circle(screen, color, center, radius)
```

#### Dessin d'une ligne :

```python
pygame.draw.line(screen, color, start_pos, end_pos, width)
```

### Dessin d'images

Pygame prend en charge le chargement et l'affichage d'images à partir de fichiers. Vous pouvez utiliser des images pour créer des personnages, des objets, des arrière-plans et d'autres éléments visuels dans votre jeu.

Voici comment charger et afficher une image dans Pygame :

```python
image = pygame.image.load("nom_de_l_image.png")
screen.blit(image, (x, y))
```

### Dessin de texte

Pygame permet également de dessiner du texte sur l'écran. Vous pouvez utiliser cette fonctionnalité pour afficher des scores, des messages, des instructions et d'autres informations textuelles dans votre jeu.

Voici comment dessiner du texte dans Pygame :

```python
font = pygame.font.Font(None, taille_police)
texte_surface = font.render("Texte à afficher", True, couleur_texte)
screen.blit(texte_surface, (x, y))
```

### Conclusion

Le dessin sur l'écran est une partie essentielle du développement de jeux avec Pygame. En utilisant les fonctions de dessin fournies par Pygame, vous pouvez créer des éléments visuels attrayants et fonctionnels pour votre jeu. N'hésitez pas à expérimenter avec différentes formes, images et styles de texte pour donner vie à votre jeu !


## Gestion du son

Pygame offre des fonctionnalités pour charger, jouer et contrôler des fichiers audio dans votre jeu. Cela vous permet d'ajouter des effets sonores, de la musique de fond et d'autres éléments audio pour améliorer l'expérience de jeu.

### Chargement de fichiers audio

Pygame peut charger plusieurs types de fichiers audio, y compris les fichiers WAV, MP3 et OGG. Vous pouvez utiliser la fonction `pygame.mixer.Sound()` pour charger un fichier audio à partir d'un fichier sur votre disque.

Voici comment charger un fichier audio dans Pygame :

```python
son = pygame.mixer.Sound("chemin_du_fichier_audio.wav")
```

### Lecture de fichiers audio

Une fois que vous avez chargé un fichier audio, vous pouvez le jouer à l'aide de la méthode `play()` de l'objet `pygame.mixer.Sound`.

Voici comment jouer un fichier audio dans Pygame :

```python
son.play()
```

### Contrôle du volume

Pygame vous permet de contrôler le volume du son à l'aide de la propriété `volume` de l'objet `pygame.mixer.Sound`. La valeur du volume varie de 0.0 (muet) à 1.0 (plein volume).

Voici comment ajuster le volume d'un son dans Pygame :

```python
son.set_volume(0.5)  # Réglez le volume à 50%
```

### Arrêt de la lecture

Vous pouvez arrêter la lecture d'un son à tout moment en appelant la méthode `stop()` de l'objet `pygame.mixer.Sound`.

Voici comment arrêter la lecture d'un son dans Pygame :

```python
son.stop()
```

### Conclusion

La gestion du son est une composante importante de l'expérience de jeu. En utilisant les fonctionnalités audio de Pygame, vous pouvez ajouter des effets sonores, de la musique de fond et d'autres éléments audio pour améliorer l'immersion et l'attrait de votre jeu.





