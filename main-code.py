import pygame
import sqlite3

# 1. Initialisation de Pygame
pygame.init()
info = pygame.display.Info()

# 2. Création de la fenêtre (largeur, hauteur)

screen_w = info.current_w
screen_h = info.current_h

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Guitar Hero")

# Horloge pour contrôler les FPS (images par seconde)
clock = pygame.time.Clock()
play = True

# 3. Boucle principale du jeu
while play:
    # Gestion des événements (clavier, souris, fermeture)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False

    # Remplissage de l'écran en noir (code couleur RGB)
    screen.fill((0, 0, 0))

    # --- Dessinez vos objets ici ---

    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limite à 60 images par seconde
    clock.tick(60)

# 4. Fermeture propre
pygame.quit()