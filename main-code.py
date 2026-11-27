import pygame
import sqlite3
import time
#import RPI.GPIO as GPIO
#from grove.grove_button import GroveButton

# Initialisation de Pygame
pygame.init()
info = pygame.display.Info()

# Création de la fenêtre de jeu (largeur, hauteur)

screen_w = info.current_w
screen_h = info.current_h

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Guitar Hero")

# Horloge pour contrôler les FPS (images par seconde)
clock = pygame.time.Clock()

# Initialisation des variables

# Global
play = True

# Formulaire
font = pygame.font.Font(None, 32)
champ_actif = False
id_input = ""
form = True

# Menu
menu = False
largeur_bouton = 280
hauteur_bouton = 60
espacement = 16
y = 0

hauteur_menu = 3 * hauteur_bouton + 2 * espacement
x_menu = (screen_w - largeur_bouton) // 2
y_menu = (screen_h - hauteur_menu) // 2

# Boucle principale du jeu
while play:
    # Variables
    position_souris = pygame.mouse.get_pos()
    survole_bouton = False
    # Gestion des événements (clavier, souris, fermeture, ...)
    for event in pygame.event.get():
        # Quitter le jeu
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                play = False

    # Affichage
    screen.fill("white")

    # Menu
    while menu:

        # Variables
        position_souris = pygame.mouse.get_pos()

        # Evenements
        for event in pygame.event.get():
            # Quitter le jeu
            if event.type == pygame.QUIT:
                menu = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu = False
            if pygame.Rect(x_menu, y1, largeur_bouton, hauteur_bouton).collidepoint(position_souris):
                survole_bouton = True
            elif pygame.Rect(x_menu, y2, largeur_bouton, hauteur_bouton).collidepoint(position_souris):
                survole_bouton = True
            elif pygame.Rect(x_menu, y3, largeur_bouton, hauteur_bouton).collidepoint(position_souris):
                survole_bouton = True
            else:
                survole_bouton = False

        # Affichage
        screen.fill("white")

        y1 = y_menu + 0 * (hauteur_bouton + espacement)
        pygame.draw.rect(screen, ("blue"), pygame.Rect(x_menu, y1, largeur_bouton, hauteur_bouton), border_radius=12)
        texte = font.render("Jouer", True, (255, 255, 255))
        screen.blit(texte, texte.get_rect(center=pygame.Rect(x_menu, y1, largeur_bouton, hauteur_bouton).center))

        y2 = y_menu + 1 * (hauteur_bouton + espacement)
        pygame.draw.rect(screen, ("grey"), pygame.Rect(x_menu, y2, largeur_bouton, hauteur_bouton), border_radius=12)
        texte = font.render("Voir les scores", True, (255, 255, 255))
        screen.blit(texte, texte.get_rect(center=pygame.Rect(x_menu, y2, largeur_bouton, hauteur_bouton).center))
        
        y3 = y_menu + 2 * (hauteur_bouton + espacement)
        pygame.draw.rect(screen, ("grey"), pygame.Rect(x_menu, y3, largeur_bouton, hauteur_bouton), border_radius=12)
        texte = font.render("S'identifier", True, (255, 255, 255))
        screen.blit(texte, texte.get_rect(center=pygame.Rect(x_menu, y3, largeur_bouton, hauteur_bouton).center))
        
        if survole_bouton:
            curseur = pygame.SYSTEM_CURSOR_HAND
            pygame.mouse.set_cursor(curseur)
        else:
            curseur = pygame.SYSTEM_CURSOR_ARROW
            pygame.mouse.set_cursor(curseur)

        # Mise à jour de l'affichage
        pygame.display.flip()
            
        # Limite à 60 images par seconde
        clock.tick(60)

    # Formulaire
    while form:
        # Variables

        # Evenements
        for event in pygame.event.get():
            # Quitter le jeu
            if event.type == pygame.QUIT:
                form = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    form = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                champ_actif = pygame.Rect(140, 80, 240, 40).collidepoint(event.pos)
            elif event.type == pygame.KEYDOWN and champ_actif:
                if event.key == (pygame.K_RETURN or pygame.K_KP_ENTER):
                    resultat = id_input
                    champ_actif = False
                elif event.key == pygame.K_BACKSPACE:
                    id_input = id_input[:-1]
                else:
                    if event.unicode.isprintable():
                        id_input += event.unicode

        # Affichage
        screen.fill("white")

        if champ_actif == False:
            txt = "Identifiant"
        else:
            txt = id_input
        screen.blit(font.render(txt, True, "black"), (60, 87))
        pygame.draw.rect(screen, "blue" if champ_actif else "gray", pygame.Rect(140, 80, 240, 40), 2)
        pygame.draw.rect(screen, "green", pygame.Rect(180, 160, 140, 45), border_radius=8)
        texte = font.render("Envoyer", True, "white")
        screen.blit(texte, texte.get_rect(center=pygame.Rect(180, 160, 140, 45).center))

        # Mise à jour de l'affichage
        pygame.display.flip()
            
        # Limite à 60 images par seconde
        clock.tick(60)

    # Mise à jour de l'affichage
    pygame.display.flip()
    
    # Limite à 60 images par seconde
    clock.tick(60)

# Fermeture propre
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


