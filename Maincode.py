import math
from random import randint
import pygame
import winsound
import time
import os
import sys

# intialiaze pygame
pygame.init()
from sys import exit

#Functions
sound_playing = 0
def gps():
    global score
    global gps_grav
    GreenPipe_rect.bottom += gps_grav
    screen.blit(GreenPipe, GreenPipe_rect)
    if GreenPipe_rect.colliderect(player_rect):
        winsound.PlaySound("sounds/idk.wav", winsound.SND_ASYNC)
        score += 1
    if GreenPipe_rect.top >= Height:
        GreenPipe_rect.bottom = -100
        GreenPipe_rect.x = randint(0,548)
        gps_grav = 0
def rps():
    global score
    global rps_grav
    RedPipe_rect.bottom += rps_grav
    screen.blit(RedPipe, RedPipe_rect)
    if RedPipe_rect.colliderect(player_rect):
        winsound.PlaySound("sounds/hit.wav", winsound.SND_ASYNC)
        score += -4
    if RedPipe_rect.top >= Height:
        RedPipe_rect.bottom = -100
        RedPipe_rect.x = randint(0,548)
        rps_grav = 0

path = "score.txt"
if os.path.exists(path) and os.path.isfile(path):
    pass

else:
    with open('highscore.dat', "w") as file:
        file.write("0")

fullscreen = False
# Screen
Width = 700
Height = 500
if fullscreen:
    screen = pygame.display.set_mode((Width, Height), pygame.FULLSCREEN)
if not fullscreen:
    screen = pygame.display.set_mode((Width, Height))

test_font = pygame.font.Font("fonts/Pixels.ttf", 90)
test_font2 = pygame.font.Font("fonts/Pixels.ttf", 150)

# clock
clock = pygame.time.Clock()

# title
pygame.display.set_caption("Pipes are falling!")

# icon

# surfaces and rectangles
bg = pygame.image.load("Graphics/background.png")

go = pygame.image.load("Graphics/gm.png")

player = pygame.image.load("Graphics/player.png")
x_pos = 250
y_pos = 450
player_rect = player.get_rect(center = (x_pos, y_pos))
player_grav = 0
player_speed = 10


GreenPipe = pygame.image.load("Graphics/GP.png")
GreenPipe_rect = GreenPipe.get_rect(midbottom = (randint(0,700), -100))

RedPipe = pygame.image.load("Graphics/RP.png")
RedPipe_rect = RedPipe.get_rect(midbottom = (randint(0,700), -100))

gps_grav = 0
rps_grav = 0

ground = pygame.image.load("Graphics/Ground.png")
ground_rect = ground.get_rect(center = (350,500))

mnbg = pygame.image.load("Graphics/mainmenu.png")

Start = pygame.image.load("Graphics/Start.png")
Start_rect = Start.get_rect(center = (348, 200))

qt = pygame.image.load("Graphics/quit.png")
qt_rect = qt.get_rect(center = (348, 350))

on = pygame.image.load("Graphics/on.png")
on_rect = on.get_rect(midbottom = (305,500))

off = pygame.image.load("Graphics/off.png")
off_rect = off.get_rect(midbottom = (305,500))

score = 0
def scorepls():
    score_surf = test_font.render(str(score), True, 'Black')
    score_rect = score_surf.get_rect(center = (50,10))
    screen.blit(score_surf, score_rect)

# loop
goc = False
mainmenu = True
running = True
game_active = False
keys = pygame.key.get_pressed()
sound_playing = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and mainmenu:
            if Start_rect.collidepoint(event.pos):
                winsound.PlaySound("sounds/select.wav", winsound.SND_ASYNC)
                game_active = True
                goc = False
                mainmenu = False
            if qt_rect.collidepoint(event.pos):
                quit()
            if off_rect.collidepoint(event.pos):
                fullscreen = True
            if on_rect.collidepoint(event.pos):
                fullscreen = False
        elif event.type == pygame.QUIT:
            running = False
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not game_active:
            player_rect.x = 300
            player_rect.bottom = ground_rect.top
            sound_playing = 0
            score = 0
            GreenPipe_rect.bottom = -100
            GreenPipe_rect.x = randint(0, 700)
            RedPipe_rect.bottom = -100
            RedPipe_rect.x = randint(0, 700)
            gps_grav = 0
            rps_grav = 0
            player_grav = 0
            game_active = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not game_active:
            goc = False
            mainmenu = True
            running = True
            game_active = False
            player_rect.x = 300
            player_rect.bottom = ground_rect.top
            sound_playing = 0
            score = 0
            GreenPipe_rect.bottom = -100
            GreenPipe_rect.x = randint(0, 700)
            RedPipe_rect.bottom = -100
            RedPipe_rect.x = randint(0, 700)
            gps_grav = 0
            rps_grav = 0
            player_grav = 0
    if game_active:
        if score <= -1:
            game_active = False
            goc = True
        rps_grav += 0.35
        gps_grav += 0.35
        player_grav += 0.8
        player_rect.bottom += player_grav
        if player_rect.bottom >= ground_rect.top:
            player_rect.bottom = ground_rect.top
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_rect.bottom == ground_rect.top:
            winsound.PlaySound("sounds/jump.wav", winsound.SND_ASYNC)
            player_grav = -20
        if keys[pygame.K_RIGHT] and player_rect.x <= 622:
            player_rect.x += 1 * player_speed
        if keys[pygame.K_LEFT] and player_rect.x >= 0:
            player_rect.x += -1 * player_speed



        screen.blit(bg, (0,0))
        screen.blit(player,player_rect)
        screen.blit(ground,ground_rect)
        scorepls()
        # Collisions

        gps()
        rps()
        if GreenPipe_rect.colliderect(RedPipe_rect):
            GreenPipe_rect.x = randint(0,700)
        if GreenPipe_rect.x >= Width:
            GreenPipe.x = Width
        if RedPipe_rect.x >= Width:
            RedPipe_rect.x = Width

        with open("highscore.dat") as file:
            highscore = int(file.read())
            if highscore <= score:
                with open("highscore.dat","w") as file:
                    file.write(str(score))

    if not game_active:
        if sound_playing == 0:
            winsound.PlaySound("sounds/gameover.wav", winsound.SND_ASYNC)
        sound_playing = 1
        if goc:
            screen.blit(go, (0,0))

    if mainmenu:
        screen.blit(mnbg, (0,0))
        screen.blit(Start, Start_rect)
        screen.blit(qt, qt_rect)

        if fullscreen:
            screen.blit(on, on_rect)
        else: screen.blit(off, off_rect)


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)






