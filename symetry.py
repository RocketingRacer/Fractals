import pygame
pygame.init()
from random import randint
import math
screen = 0
color = (255,255,255)
symetry = 16
class Point:
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.pos = [x,y]
        self.r = r
        self.travel = True
        self.nodraw = True
    def dist(self,p2):
        return math.sqrt(pow(self.pos[0]-p2.pos[0],2)+pow(self.pos[1]-p2.pos[1],2))
    def update(self,particles):
        relevent= list(set().union(particles[(self.pos[0]-1)//10],particles[self.pos[0]//10],particles[(self.pos[0]+1)//10]))
        coliding = False
        for p in relevent:
            if self.dist(p) < p.r+self.r:
                coliding = True
                self.nodraw = False
                break
        if self.pos[0]<self.r or coliding: #stop condions ie coliding or edge
            self.travel=False
            return False
        if self.travel:
            self.pos = [self.pos[0]-1,self.pos[1]+randint(-2,2)]
            #print(self.pos)
        return True

    def show(self):
        global tree
        global screen
        if not self.nodraw:
            pygame.draw.circle(tree,color,self.pos,self.r)

            for i in range(symetry):

                RotatedTree=pygame.transform.rotate(tree,int((360/symetry)*i))
                RotatedScaledTree=pygame.transform.scale(RotatedTree,(dimensions[0],dimensions[1]))
                #print((360/symetry)*i)
                RotatedScaledTree.set_colorkey((0,0,0))
                screen.blit(RotatedScaledTree,(0,0))

        #else:
        #    pygame.draw.circle(tree,(255,0,0),self.pos,self.r)
        #    scaledTree = pygame.transform.scale(tree,(dimensions[0]//2,dimensions[1]//2))
        #    screen.blit(scaledTree,(dimensions[0]//2,dimensions[1]//2-dimensions[1]//4))


dimensions = (1000,1000)
tree =0
def main():
    global tree
    global screen
    screen = pygame.display.set_mode(dimensions)
    tree = pygame.Surface(dimensions)
    particles = [[]for i in range(dimensions[0]//10+3)]
    root = Point(dimensions[0]//2,dimensions[1]//2,15)
    root.nodraw = False
    root.show()
    particles[int(root.pos[0]/10)].append(root)
    pygame.display.flip()
    for i in range(10000):
        p = Point(dimensions[0],dimensions[1]//2,2)
        start_pos = p.pos
        while p.update(particles):
            for EVENT in pygame.event.get():
                if EVENT.type == pygame.QUIT:
                    exit()
                if EVENT.type == pygame.KEYDOWN:
                    if EVENT.key == pygame.K_ESCAPE:
                        exit()
        p.show()
        if not p.nodraw:
            particles[int(p.pos[0]/10)].append(p)
        if abs(p.pos[0] - start_pos[0]) < 5:
            if abs( p.pos[1] - start_pos[1])<5:
                break
        pygame.display.flip()


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
