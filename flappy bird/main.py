import pygame
import random

#wywołanie pygame
pygame.init()

#do startu
FPS = 60
WIDTH = 400
HEIGHT = 600
Clock = pygame.time.Clock()
Run = True
Window = pygame.display.set_mode((WIDTH, HEIGHT))

#ładowanie obrazków
ptaszor_png = pygame.image.load('assets\Ptaszor.png')
new_scale = 70, 70
scaled_ptaszor = pygame.transform.scale(ptaszor_png, new_scale)

#zmienne gracza
player_Y = HEIGHT//2
player_X = 50
player_speed = 5
gravity = 0.09
player_velocity_y = 0
is_jump = True

#hitboxy gracza
player_hitbox = player_X, player_X, scaled_ptaszor

#pętla gry
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            Run = False 

    #grawitacja gracza
    player_Y += player_velocity_y
    player_velocity_y += gravity

    #wypełnienie tła
    Window.fill((0, 0, 0))

    #sterowanie gracza
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        player_Y -= player_speed
        gravity = 0

    #rysowanie obrazków
    player = Window.blit(scaled_ptaszor, (player_X, player_Y))

    #ustalenie FPS'sów
    Clock.tick(FPS)

    #odświeżanie ekranu
    pygame.display.flip()