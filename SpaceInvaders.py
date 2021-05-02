import pygame
import random
import math
from pygame import mixer

pygame.init()
FPS = 60
fpsClock = pygame.time.Clock()

# Make Screen
screen = pygame.display.set_mode((800, 600))

# Background Fucntion
backgroundImg = pygame.image.load('background.png')
backgroundX = 0
backgroundY = 0
def drawBackground(x, y):
    screen.blit(backgroundImg, (x, y))

# Spaceship Function
spaceshipImg = pygame.image.load('spaceship.png')
spaceshipX = 370
spaceshipY = 500
spaceshipChange = 0
def drawSpaceship(x, y):
    screen.blit(spaceshipImg, (x, y))

# Laser Function
laserImg = pygame.image.load('laser.png')
laserX = 0
laserY = 0
laserChange = -7
laserState = 'ready'
def drawLaser(x, y):
    screen.blit(laserImg, (laserX, laserY))

# Ufo Function
ufoImg = []
ufoX = []
ufoY = []
ufoChangeX = []
for i in range(6):
    ufoImg.append(pygame.image.load('ufo.png'))
    ufoX.append(random.randint(-13, 750))
    ufoY.append(random.randint(-10, 150))
    ufoChangeX.append(4)
def drawUfo(x, y):
    screen.blit(ufoImg[i], (x, y))

# Collision Function
def collision(ufoX, ufoY, laserX, laserY):
    if (laserY >= ufoY and laserY <= (ufoY + 32))  and (laserX >= (ufoX - 10) and laserX <= (ufoX + 40)):
            return True
    else:
        return False

# Explosion Function
explosionX = 0
explosionY = 0
count = 0
count1 = 0
explosionImg = [] 
for i in range(9):
    explosionImg.append(pygame.image.load('explosion1.png'))
explosionImg[0] = pygame.image.load('explosion1.png')
explosionImg[1] = pygame.image.load('explosion2.png')
explosionImg[2] = pygame.image.load('explosion3.png')
explosionImg[3] = pygame.image.load('explosion4.png')
explosionImg[4] = pygame.image.load('explosion5.png')
explosionImg[5] = pygame.image.load('explosion6.png')
explosionImg[6] = pygame.image.load('explosion7.png')
explosionImg[7] = pygame.image.load('explosion8.png')
explosionImg[8] = pygame.image.load('explosion9.png')
def explosion(x, y, point):
    screen.blit(explosionImg[point], (x, y))
    
# Enemy bullet function
bulletImg = pygame.image.load('bullet.png')
bulletX = []
bulletY = []
bulletChangeY = 7
bulletState = []
for i in range(6):
    bulletX.append(0)
    bulletY.append(0)
    bulletState.append('ready')
def drawBullet(x, y):
    screen.blit(bulletImg, (x, y))
def bullet():
    number = random.randint(1, 100)
    if number == 1:
        return True
    else:
        return False

# Bullet collision function
def bulletCollision(spaceshipX, spaceshipY, bullletX, bulletY):
    if (bulletY[i] >= spaceshipY and bulletY[i] <= (spaceshipY + 32)) and (bulletX[i] >= (spaceshipX - 10) and bulletX[i] <= (spaceshipX + 40)):
        return True
    else:
        return False

# Bullet Explosion
bulletExplosionX = 0
bulletExplosionY = 0
bulletCount = 0
bulletCount1 = 0
bulletExplosionImg = [] 
for i in range(9):
    bulletExplosionImg.append(pygame.image.load('explosion1.png'))
bulletExplosionImg[0] = pygame.image.load('explosion1.png')
bulletExplosionImg[1] = pygame.image.load('explosion2.png')
bulletExplosionImg[2] = pygame.image.load('explosion3.png')
bulletExplosionImg[3] = pygame.image.load('explosion4.png')
bulletExplosionImg[4] = pygame.image.load('explosion5.png')
bulletExplosionImg[5] = pygame.image.load('explosion6.png')
bulletExplosionImg[6] = pygame.image.load('explosion7.png')
bulletExplosionImg[7] = pygame.image.load('explosion8.png')
bulletExplosionImg[8] = pygame.image.load('explosion9.png')
def bulletExplosion(x, y, point):
    screen.blit(bulletExplosionImg[point], (x, y))

# Score Function
font = pygame.font.SysFont('Arial', 32)
textX = 10
textY = 10
def score_cal(x, y):
    score_value = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))

# Health Function
fontHealth = pygame.font.SysFont('Arial', 32)
healthTextX = 630
healthTextY = 10
def health_cal(x, y):
    health_value = font.render("Health : " + str(health), True, (255, 255, 255))
    screen.blit(health_value, (x, y))

# Fort Explosion Function
fortExplosionX = []
fortExplosionY = []
fortExplosionImg = []
fortCount = 0
fortCount1 = 0
for i in range(9):
    fortExplosionImg.append(pygame.image.load('explosion1.png'))
for i in range(4):
    fortExplosionX.append(0)
for i in range(2):
    fortExplosionY.append(0)
fortExplosionX[0] = 400
fortExplosionX[1] = 20
fortExplosionX[2] = 600
fortExplosionX[3] = 200
fortExplosionY[0] = 350
fortExplosionY[1] = 500
fortExplosionImg[0] = pygame.image.load('explosion1.png')
fortExplosionImg[1] = pygame.image.load('explosion2.png')
fortExplosionImg[2] = pygame.image.load('explosion3.png')
fortExplosionImg[3] = pygame.image.load('explosion4.png')
fortExplosionImg[4] = pygame.image.load('explosion5.png')
fortExplosionImg[5] = pygame.image.load('explosion6.png')
fortExplosionImg[6] = pygame.image.load('explosion7.png')
fortExplosionImg[7] = pygame.image.load('explosion8.png')
fortExplosionImg[8] = pygame.image.load('explosion9.png')
def fortExplosion(x, y, point):
    screen.blit(fortExplosionImg[point], (x, y))

# Fort Function
fortImg = []
fortX = []
fortY = []
for i in range(4):
    fortImg.append(pygame.image.load('fort1.png'))
    fortX.append(0)
    fortY.append(350)
fortImg[0] = pygame.image.load('fort1.png')
fortImg[1] = pygame.image.load('fort2.png')
fortImg[2] = pygame.image.load('fort3.png')
fortImg[3] = pygame.image.load('fort4.png')
fortX[0] = 400
fortX[1] = 20
fortX[2] = 600
fortX[3] = 200
def drawFort(x, y):
    screen.blit(fortImg[i], (x, y))

# Gameover Function
overX = 300
overY = 100
overImg = pygame.image.load('gameover.png')
def over(x, y):
    screen.blit(overImg, (x, y))

# Main Program
gameOver = False
health = 100
running = True
hit = False
bulletHit = False
score = 0
while running:
    score_cal(textX, textY)
    health_cal(healthTextX, healthTextY)
    screen.fill((0, 0, 0))
    drawBackground(backgroundX, backgroundY)
    for i in range(4):
        drawFort(fortX[i], fortY[i])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                spaceshipChange = 5
            if event.key == pygame.K_a:
                spaceshipChange = -5
            if event.key == pygame.K_SPACE:
                if laserState == 'ready':
                    laserX = spaceshipX + 10
                    laserY = spaceshipY - 50
                    laserState = 'fire'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_a:
                spaceshipChange = 0
    if spaceshipX <= -13:
        spaceshipX = -13
    if spaceshipX >= 750:
        spaceshipX = 750
    drawSpaceship(spaceshipX, spaceshipY)
    for i in range(6):
        if ufoX[i] <= -13:
            ufoChangeX[i] = 4
            ufoY[i] += 30
        if ufoX[i] >= 750:
            ufoChangeX[i] = -4
            ufoY[i] += 30
        ufoX[i] += ufoChangeX[i]
        drawUfo(ufoX[i], ufoY[i])
        if ufoY[i] >= 350:
            gameOver = True
    for i in range(6):
        if bullet() == True and bulletState[i] == 'ready':
            bulletX[i] = ufoX[i]
            bulletY[i] = ufoY[i] + 20
            bulletState[i] = 'fire'
        drawBullet(bulletX[i], bulletY[i])
        bulletY[i] += bulletChangeY
        if bulletY[i] >= 750:
            bulletState[i] = 'ready'
            bulletY[i] = -100
            bulletX[i] = -100
    if laserState == 'fire':
        drawLaser(laserX, laserY)
    spaceshipX += spaceshipChange
    laserY += laserChange
    if laserY <= -10:
        laserX = 0
        laserY = 0
        laserState = 'ready'
    for i in range(6):
        if collision(ufoX[i], ufoY[i], laserX, laserY) == True:
            laserX = -100
            laserY = -100
            laserState = 'ready'
            explosionX = ufoX[i] - 30
            explosionY = ufoY[i] - 30
            ufoX[i] = random.randint(-13, 750)
            ufoY[i] = random.randint(-10, 150)
            hit = True
            score += 1
        if collision(spaceshipX, spaceshipY, bulletX[i], bulletY[i]) == True:
            bulletX[i] = -100
            bulletY[i] = -100
            bulletState[i] = 'ready'
            bulletExplosionX = spaceshipX - 40
            bulletExplosionY = spaceshipY
            bulletHit = True
            health -= 20
    if hit == True:
        explosion(explosionX, explosionY,  count)
        if count1%4 == 0:
            count += 1
        count1 += 1
    if count >= 8:
        count = 0
        hit = False
    if bulletHit == True:
        bulletExplosion(bulletExplosionX, bulletExplosionY, bulletCount)
        if bulletCount1%4 == 0:
            bulletCount += 1
        bulletCount1 += 1
    if bulletCount >= 8:
        bulletCount = 0
        bulletHit = False
    if gameOver == True or health == 0:
        spaceshipChange = 0
        laserChange = 0
        bulletChangeY = 0
        for i in range(6):
            ufoChangeX[i] = 0
        for x in range(4):
            for y in range(2): 
                fortExplosion(fortExplosionX[x], fortExplosionY[y], fortCount)
                fortCount1 += 1
        if fortCount1%6 == 0:
            fortCount += 1
        if fortCount >= 8:
            fortCount = 0
        over(overX, overY)
    score_cal(textX, textY)
    health_cal(healthTextX, healthTextY)
    pygame.display.update()
    fpsClock.tick(FPS)