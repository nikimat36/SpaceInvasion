### https://www.youtube.com/watch?v=FfWpgLFMI7w&ab_channel=freeCodeCamp.org
## time:
## *2:04:00 - game sound part - ommited 
import pygame
import random
import math

# initialising pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background image
background = pygame.image.load('C:/Users/Nikita Matysová/Desktop/NIKI/PROGRAMOVÁNÍ/python/2020 znova/OOP PY/Udemy PY/GAME/background.png')

# Title nad Icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('C:/Users/Nikita Matysová/Desktop/NIKI/PROGRAMOVÁNÍ/python/2020 znova/OOP PY/Udemy PY/GAME/bullet.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('C:/Users/Nikita Matysová/Desktop/NIKI/PROGRAMOVÁNÍ/python/2020 znova/OOP PY/Udemy PY/GAME/g-man.png')
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('C:/Users/Nikita Matysová/Desktop/NIKI/PROGRAMOVÁNÍ/python/2020 znova/OOP PY/Udemy PY/GAME/enemy.png'))
    enemyX.append(random.randint(0, 800))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(40)

# Bullet
## ready = you can not see bullet on the screen
## fire = the bullet in currently moving
bulletImg = pygame.image.load('C:/Users/Nikita Matysová/Desktop/NIKI/PROGRAMOVÁNÍ/python/2020 znova/OOP PY/Udemy PY/GAME/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0  # useless value
bulletY_change = 2
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render(" GAME OVER ", True, (0,0,0))
    screen.blit(over_text, (200, 250))   

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0,0,255))
    screen.blit(score, (x, y))

# Fce hráče
def player(x, y):
    screen.blit(playerImg, (x, y))   # blit znamená nakresli

# Fce nepřátel
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y)) 

# Fce kulky
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX ,2) + math.pow(enemyY - bulletY,2))
    if distance < 50:
        return True
    else:
        return False
# Game loop
running = True

while running:
    # screen.fill((0, 0, 100))  #background color (RGB), vždy první - před obrazky
    # background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #male quit dělá neplechu
            running = False

    # if keystroke is pressed chcekc wheter its right/left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

# ohraničení plochy pro hráče
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 760:
        playerX = 760


# enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 400:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 720:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480 
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 719)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()