import pygame
import threading
import time

sc = pygame.display.set_mode((1600, 800))
defolt = pygame.image.load("image/dle.png")
walkleft = [pygame.image.load("image/left_1.png"), pygame.image.load("image/left_2.png"), pygame.image.load("image/left_3.png"), pygame.image.load("image/left_4.png"), pygame.image.load("image/left_5.png"), pygame.image.load("image/left_6.png")]
walkright = [pygame.image.load("image/right_1.png"), pygame.image.load("image/right_2.png"), pygame.image.load("image/right_3.png"), pygame.image.load("image/right_4.png"), pygame.image.load("image/right_5.png"), pygame.image.load("image/right_6.png")]


bg = pygame.image.load("image/bg.jpg")

left = False
right = False
animcount = 0
x = 50
y = 530
w = 90
h = 90
lastmove = "right"
isF = True


clock = pygame.time.Clock()

def fire():
    global isF
    isF = False
    time.sleep(1)
    isF = True

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, sc):
        pygame.draw.circle(sc, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animcount
    if animcount + 1 >= 30:
        animcount = 0
    if left:
        sc.blit(walkleft[animcount // 5], (x, y))
        animcount += 1
    elif right:
        sc.blit(walkright[animcount // 5], (x, y))
        animcount += 1
    else:
        sc.blit(defolt, (x, y))

    for bullet in bullets:
        bullet.draw(sc)
    pygame.display.update()
    sc.blit(bg, (0, 0))



jump = False
djump = False
jumpcount = 10
djumpcount = 15
game = True

bullets = []
while game:
    clock.tick(30)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    for bullet in bullets:
        if bullet.x < 1600 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()


    if keys[pygame.K_f] and isF:
        threading.Thread(target=fire).start()
        if lastmove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 150:
            bullets.append(snaryad(round(x + w // 2), round(y + h // 2), 5, (255, 0, 0), facing))
    if keys[pygame.K_d] and x < 1500:
        x += 5
        right = True
        left = False
        lastmove = "right"
    elif keys[pygame.K_a] and x > 50:
        x -= 5
        left = True
        right = False
        lastmove = "left"
    else:
        left = False
        right = False
        animcount = 0

    if not(jump):
        if keys[pygame.K_SPACE]:
                jump = True

    else:
        if jumpcount >= -10:
            y -= jumpcount * 2
            jumpcount -= 1
        else:
            jump = False
            jumpcount = 10



    drawWindow()

