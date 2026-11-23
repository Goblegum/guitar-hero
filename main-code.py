import pygame

# 1. Initialisation de Pygame
pygame.init()

# 2. Création de la fenêtre (largeur, hauteur)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

# Horloge pour contrôler les FPS (images par seconde)
clock = pygame.time.Clock()
running = True

# 3. Boucle principale du jeu
while running:
    # Gestion des événements (clavier, souris, fermeture)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Remplissage de l'écran en noir (code couleur RGB)
    screen.fill((0, 0, 0))

    # --- Dessinez vos objets ici ---

    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limite à 60 images par seconde
    clock.tick(60)

# 4. Fermeture propre
pygame.quit()