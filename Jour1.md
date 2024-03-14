# Cours Pygame

## Introduction à Pygame

Pygame est une bibliothèque de développement de jeux en Python. Elle fournit des fonctionnalités pour créer des jeux 2D en offrant un accès facile à la gestion des graphismes, de l'audio et des entrées utilisateur.

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

Pour dessiner des formes, des images ou du texte sur l'écran, vous utilisez les fonctions de dessin fournies par Pygame, telles que `pygame.draw.rect()`, `pygame.draw.circle()`, `pygame.draw.line()`, `pygame.draw.image()`, etc.

## Gestion des images

Pour charger et afficher des images dans votre jeu, vous pouvez utiliser la classe `pygame.image.load()` pour charger l'image à partir d'un fichier, puis utiliser `blit()` pour l'afficher sur l'écran.

## Gestion du son

Pygame prend également en charge la lecture de sons. Vous pouvez charger un fichier sonore à l'aide de `pygame.mixer.Sound()` et le jouer avec la méthode `play()`.



