import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('space.png')

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('space-invaders.png')
pygame.display.set_icon(icon)

# Player
playerimg = pygame.image.load('player64by64.png')
playerX = 370
playerY = 480
playerX_change = 0

# Bullet
bulletimg = pygame.image.load('Bullet png.png')
bulletX = 0
bulletY = 480
bulletY_change = 0.7
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font(None,32)
textX = 10
textY = 10

# Game over
game_over_font = pygame.font.Font(None,64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255,0,0))
    screen.blit(over_text, (200,250))

def player(x, y):
    screen.blit(playerimg, (x, y))

def enemy(x, y, img):
    screen.blit(img, (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    return distance < 27

# Multiple enemies
num_of_enemies = 6
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load('alien type 1.jpg'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)

# Game loop
running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Player key controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy movement & collision
    for i in range(num_of_enemies):
        # Game over condition
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move enemies off screen
            game_over_text()
            break

        # Move enemy
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)

        # Draw enemy
        enemy(enemyX[i], enemyY[i], enemyimg[i])

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Draw player and score
    player(playerX, playerY)
    show_score(textX,textY)

    pygame.display.update()
