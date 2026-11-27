import pygame
import sqlite3
import time
import RPI.GPIO as GPIO
from grove.grove_button import GroveButton

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

















#partie de Bilal

"""GPIO.setmode(GPIO.BCM)

GPIO.setup(num_pin, GPIO.IN)


button = GroveButton(22)

def on_press(t):


def on_release(t):


button.on_press = on_press
button.on_release = on_release




pygame.mixer.init()
pygame.mixer.music.load("ACDC - Highway to Hell (Official Video).mp3")  # Fonctionne aussi avec un fichier .wav
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(0.5)"""


