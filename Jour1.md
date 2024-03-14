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

## Gestion des événements

Pygame utilise une file d'attente d'événements pour gérer les entrées utilisateur, telles que les clics de souris, les touches du clavier, etc. Vous pouvez les gérer dans la boucle de jeu en parcourant les événements.

## Dessin sur l'écran

Pour dessiner des formes, des images ou du texte sur l'écran, vous utilisez les fonctions de dessin fournies par Pygame, telles que `pygame.draw.rect()`, `pygame.draw.circle()`, `pygame.draw.line()`, `pygame.draw.image()`, etc.

## Gestion des images

Pour charger et afficher des images dans votre jeu, vous pouvez utiliser la classe `pygame.image.load()` pour charger l'image à partir d'un fichier, puis utiliser `blit()` pour l'afficher sur l'écran.

## Gestion du son

Pygame prend également en charge la lecture de sons. Vous pouvez charger un fichier sonore à l'aide de `pygame.mixer.Sound()` et le jouer avec la méthode `play()`.

C'est un bon point de départ pour vous familiariser avec Pygame. Avec ces bases, vous pouvez commencer à créer des jeux simples et explorer davantage les fonctionnalités avancées de la bibliothèque.


