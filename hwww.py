import pygame,sys
from pygame.locals import QUIT
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("lightbulb")

pict1= pygame.image.load("animation images/light bulb off.png")
pict1= pygame.transform.scale(pict1,(800,600))



pict2= pygame.image.load("animation images\light bulb on.png")
pict2= pygame.transform.scale(pict2,(800,600))



while True:
    screen.blit(pict1,(0,0))
    time.sleep(1)
    pygame.display.update()
    screen.blit(pict2,(0,0))
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
