import pygame
import random

# initialize pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('space.png')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('player64by64.png')
player_width = playerimg.get_width()
playerX = 370
playerY = 480
playerX_change = 0

# enemy
enemyimg = pygame.image.load('alien type 1.jpg')
enemyX = random.randint(0,600)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#bullet, ready state - cant see the bullet on the screen
bulletimg = pygame.image.load('Bullet png.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.6
bullet_state = "ready"


def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy (x, y):
    screen.blit(enemyimg, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

# Game loop
running = True
while running:

    screen.fill((0,0,0))   # clear screen

    #background image
    screen.blit(background, (0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # key pressed(speed control)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.25
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.25
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # key released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # player movement
    playerX += playerX_change

    # enforce boundaries
    playerX = max(0, min(playerX, 800 - playerimg.get_width()))

    #enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyY += enemyY_change

   # bullet movement
   if bulletY <= 0:
    bulletY = 480
    bullet_state = "ready"

   if bullet_state == "fire":
    fire_bullet(bulletX, bulletY)
    bulletY -= bulletY_change


    # draw player
    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()

