import pygame
import sqlite3
import time

pygame.init()
info = pygame.display.Info()

screen_w = info.current_w
screen_h = info.current_h
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Guitar Hero")

clock = pygame.time.Clock()
play = True

police_menu = pygame.font.Font(None, 42)
largeur_bouton = 280
hauteur_bouton = 60
espacement = 16

boutons_menu = [
    ("Jouer", (55, 95, 220)),
    ("Voir les scores", (48, 52, 66)),
    ("S’identifier", (48, 52, 66)),
]

hauteur_menu = 3 * hauteur_bouton + 2 * espacement
x_menu = (screen_w - largeur_bouton) // 2
y_menu = (screen_h - hauteur_menu) // 2

curseur_actuel = pygame.SYSTEM_CURSOR_ARROW

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            play = False

    screen.fill((0, 0, 0))
    position_souris = pygame.mouse.get_pos()
    survole_bouton = False

    for index, (libelle, couleur) in enumerate(boutons_menu):
        y = y_menu + index * (hauteur_bouton + espacement)
        bouton = pygame.Rect(x_menu, y, largeur_bouton, hauteur_bouton)

        if bouton.collidepoint(position_souris):
            survole_bouton = True

        pygame.draw.rect(screen, couleur, bouton, border_radius=12)
        texte = police_menu.render(libelle, True, (255, 255, 255))
        screen.blit(texte, texte.get_rect(center=bouton.center))

    curseur = pygame.SYSTEM_CURSOR_ARROW
    if survole_bouton:
        curseur = pygame.SYSTEM_CURSOR_HAND

    if curseur != curseur_actuel:
        pygame.mouse.set_cursor(curseur)
        curseur_actuel = curseur

    pygame.display.flip()
    clock.tick(60)

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


