import pygame
import random
pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.flip()
clock = pygame.time.Clock()
running = True
score = 0
score_hi = 0
run = 0
image  = pygame.image.load('13.png')
x1 = 0
y1 = 350
direction = 'left'
screen.blit(image, (x1, y1))
image  = pygame.image.load('13.png')
x2 = 2404
y2 = 350
direction = 'left'
screen.blit(image, (x2, y2))
image  = pygame.image.load('15.png')
dinox = 50
dinoy = 281
direction = 'left'
f = '15.png'
MYEVENTTYPE = 30
u = 5
p = 0
up = 0
k = 0
kak = 0
kt = 0
kx = 0
ky = 0
h = 0
pygame.time.set_timer(MYEVENTTYPE, 7500)
screen.blit(image, (dinox, dinoy))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if run == 0:
                    run = 1
                    u = 5
                    p = 0
                    up = 0
                    k = 0
                    kak = 0
                    kt = 0
                    kx = 0
                    ky = 0
                    h = 0
                    dinox = 50
                    dinoy = 281
                    x1 = 0
                    y1 = 350
                    x2 = 2404
                    y2 = 350
                    score = 0
                    f = '8.png'
                    MYEVENTTYPE = 30
                    pygame.time.set_timer(MYEVENTTYPE, 2500)
                else:
                    if p == 0:
                        p = 1
                        up = -18
        if event.type == MYEVENTTYPE:
            if run == 1:
                pygame.time.set_timer(MYEVENTTYPE, 2500)
                if k == 3:
                    u += 1
                    k = 0
                else:
                    k += 1
                kak = 1
                kx = 500
                ky = -1
                h = -1
                kt = random.randint(1, 4)
                if ky == -1:
                    if kt == 1:
                        ky = 296
                    if kt != 1:
                        ky = 281
                if h == -1:
                    if kt == 1:
                        h = 36
                    if kt == 2:
                        h = 51
                    if kt == 3:
                        h = 96
                    if kt == 4:
                        h = 144
    screen.fill((255, 255, 255))
    if run == 1:
        x1 -= u
        x2 -= u
        if kak == 1:
            kx -= u
        score += u
        if f == '9.png':
            f = '8.png'
        else:
            f = '9.png'
    f1 = pygame.font.Font(None, 24)
    text1 = f1.render('score: ' + str(score // 100), 1, (180, 0, 0))
    f2 = pygame.font.Font(None, 24)
    text2 = f2.render('hi_score: ' + str(score_hi // 100), 1, (180, 0, 0))
    if x1 <= -2404:
        x1 = 2404
    if x2 <= -2404:
        x2 = 2404
    if p == 1:
        up += 0.1
        dinoy += up
        if dinoy <= 71:
            dinoy = 41
            p = 2
            up = 0
    if p == 2:
        up += 0.1
        dinoy += up
        if dinoy >= 281:
            dinoy = 281
            p = 0
            up = 0
    
    direction = 'left'
    image  = pygame.image.load('13.png')
    screen.blit(image, (x1, y1))
    image  = pygame.image.load('13.png')
    screen.blit(image, (x2, y2))
    image  = pygame.image.load(f)
    screen.blit(image, (dinox, dinoy))
    screen.blit(text1, (10, 10))
    screen.blit(text2, (260, 10))
    if kak == 1:
        image  = pygame.image.load(str(2 + kt) + '.png')
        screen.blit(image, (kx, ky))
    if ((dinox + 87 >= kx and dinox + 87 <= kx + h) or (dinox <= kx + h and dinox >= kx)) and dinoy + 94 >= ky:
        run = 0
        image  = pygame.image.load('7.png')
        screen.blit(image, (61, 100))
        image  = pygame.image.load('14.png')
        screen.blit(image, (61, 214))
        t = score
        score_hi = max(t, score_hi)
        p = 0
        kak = 0
    if kx <= -h:
        kak = 0
    clock.tick(500)
    pygame.display.flip()