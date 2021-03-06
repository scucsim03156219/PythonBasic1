'''
兩球會互相碰撞，碰撞期間發生聲音
by Ching-Shoei Chiang
'''
import random, pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()
# set up the window
WINDOWWIDTH = 800
WINDOWHEIGHT = 800
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('object moving')
WHITE = (255, 255, 255)
WAVFILE = "badswap.wav"
s = pygame.mixer.Sound(WAVFILE)
circle1Img = pygame.image.load('circle64.png')
circle2Img = pygame.image.load('redcircle.jpg')
circle1x = circle1y = 600
circle2x = circle2y = 200
dir1x = -1
dir1y = -1
dir2x = 1
dir2y = 1
step = 10
coll = False

def overlap(a,b,c,d):
    return  not (a+b<c or c+d<a)

def collision_detection(x1, y1, w1, h1, x2, y2, w2, h2):
    return overlap(x1, w1, x2, w2) and overlap(y1, h1, y2, h2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:                                                    
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                 pygame.quit()
                 sys.exit()
# Move the first circle
    if circle1y>WINDOWHEIGHT-64 or circle1y<0:
        dir1y = -1 * dir1y
    if circle1x>WINDOWWIDTH-64 or circle1x<0:
        dir1x = -1 * dir1x
    circle1x = circle1x + dir1x*step
    circle1y = circle1y + dir1y*step

# Move the second circle
    if circle2y>WINDOWHEIGHT-64 or circle2y<0:
        dir2y = -1 * dir2y
    if circle2x>WINDOWWIDTH-64 or circle2x<0:
        dir2x = -1 * dir2x
    circle2x = circle2x + dir2x*step
    circle2y = circle2y + dir2y*step
# Collision Detection
    collision = collision_detection(circle1x, circle1y, 64, 64, circle2x, circle2y, 64, 64)
    if not collision and coll:
        coll = False
    if collision and not coll:
        ch = s.play()
#        while ch.get_busy():
#            pygame.time.delay(10)
        coll = True
    
    screen.fill(WHITE)
    screen.blit(circle1Img, (circle1x, circle1y))
    screen.blit(circle2Img, (circle2x, circle2y))
    pygame.display.update()

    fpsClock.tick(FPS)
