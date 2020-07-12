import pygame
pygame.init()
from random import randint
import math
screen = 0
color = (255,255,255)
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.pos = [x,y]
        self.r = 2
        self.travel = True
    def dist(self,p2):
        return math.sqrt(pow(self.pos[0]-p2.pos[0],2)+pow(self.pos[1]-p2.pos[1],2))
    def update(self,particles):
        relevent= list(set().union(particles[(self.pos[0]-1)//10],particles[self.pos[0]//10],particles[(self.pos[0]+1)//10]))

        coliding = False
        for p in relevent:
            if self.dist(p) < p.r+self.r:
                coliding = True
                break
        if self.pos[0]<self.r or coliding: #stop condions ie coliding or edge
            self.travel=False
            return False
        if self.travel:
            self.pos = [self.pos[0]-1,self.pos[1]+randint(-3,3)]
            #print(self.pos)dimensions[1]//2
        return True

    def show(self):
        global tree
        global screen
        pygame.draw.circle(tree,color,self.pos,self.r)
        screen.blit(tree,(0,0))

dimensions = (1000,1000)
tree =0
def main():
    global tree
    global screen
    screen = pygame.display.set_mode(dimensions)
    tree = pygame.Surface(dimensions)
    particles = [[]for i in range(dimensions[0]//10+3)]
    root = Point(0,dimensions[1]//2)
    root.show()
    particles[int(root.pos[0]/10)].append(root)
    pygame.display.flip()
    for i in range(1000000):
        p = Point(dimensions[0],dimensions[1]//2)
        start_pos = p.pos
        while p.update(particles):
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    exit()
                if EVENT.type == pygame.KEYDOWN:
                    if EVENT.key == pygame.K_ESCAPE:
                        exit()
        p.show()
        if abs(p.pos[0] - start_pos[0]) < 5:
            if abs( p.pos[1] - start_pos[1])<5:
                break
        pygame.display.flip()
        particles[int(p.pos[0]/10)].append(p)

    print("Done")
    while -1:
        pygame.time.wait(100)
        for EVENT in pygame.event.get():
            if EVENT.type == pygame.QUIT:
                exit()
            if EVENT.type == pygame.KEYDOWN:
                if EVENT.key == pygame.K_ESCAPE:
                    exit()

main()
