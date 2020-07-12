import math
import pygame
angle = 0
position = [100,700]
def line(a,angle,screen):
    global position
    x = position[0]+a*math.cos(math.radians(angle))
    y = position[1]+a*math.sin(math.radians(angle))
    pygame.draw.line(screen,(255,255,255),position,(x,y),3)
    pygame.display.flip()
    #pygame.time.wait(500)
    position = [x,y]
def flake(a,screen,order):
    global angle
    global position
    if order > 0:
        for t in [60, -120, 60, 0]:
            #print(angle)
            flake(a/3,screen,order-1)
            angle = angle + t
    else:
        line(a,angle,screen)


pygame.init()
screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Koch Flake")
for z in range (6):
    for i in range(3):
        flake(800,screen,z)
        angle = angle-120
    pygame.image.save(screen,str(z)+".png")
    screen.fill((0,0,0))

pygame.display.flip()
while -1:
    pygame.time.wait(100)
    for EVENT in pygame.event.get():
        if EVENT.type == pygame.QUIT:
            exit()
        if EVENT.type == pygame.KEYDOWN:
            if EVENT.key == pygame.K_ESCAPE:
                exit()
