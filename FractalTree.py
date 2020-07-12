#!usr/bin/env python3
import pygame
import math
from random import randint
import colorsys
from glob import glob
import os
pygame.init()
CUTOFF = 10
down = 30
maxSplits = 2
baseSplit = 3
colTop = 500
lengthDelta = .9
branchLength=120
TrunkHeight = 150
colorHSV = [0,.8,.8]
background = (0,0,0)
startLineWeight = 7
constant = 4
screen = 0

saving = False
x = 1920
y = 1080

class Branch:

    def __init__(self,root,top,length,angle):
        self.angle = angle
        self.root = root
        self.length = length
        self.top = top
def main():
    folderCount = 0
    if saving == True:
        folderCount = len(glob("trees/*/"))
        print(folderCount)
        os.mkdir("trees/"+str(folderCount))
    global screen
    global x
    global down
    x = x//2
    screen = pygame.display.set_mode((x*2,y),pygame.FULLSCREEN)
    screen.fill(background)

    source = Branch((0,0),(0,TrunkHeight),branchLength,90)
    drawLine(source.root,source.top,startLineWeight)
    for i in range(baseSplit):
        makeBranch(source,i%2,startLineWeight)
    z=1

    while z < 1000:
        print("TreeNumber",z,"done.")
        if saving == True:
            pygame.image.save(screen,"trees/"+str(folderCount)+"/TreeNumber"+str(z).rjust(4,"0")+".jpg")
        z=z+1
        screen.fill(background)
        down = randint(10,40)
        source = Branch((0,0),(0,TrunkHeight),branchLength,90)
        drawLine(source.root,source.top,startLineWeight)
        for i in range(baseSplit):
            makeBranch(source,i%2,startLineWeight)

def drawLine(p1,p2,weight):
    global screen
    #pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    #colorRGB = colorsys.hsv_to_rgb(colorHSV[0],colorHSV[1],colorHSV[2])
    #colorRGB = [colorRGB[x]*255 for x in range(3)]
    colorRGB = [160,int(min(p1[1]/colTop,1)*173)+82,45]
    pygame.draw.line(screen, colorRGB, (p1[0]+x,y-p1[1]), (p2[0]+x,y-p2[1]),weight)
    #colorHSV[0] = colorHSV[0]+0.01
    pygame.display.update()
def makeBranch(SourceBranch,direction,weight):
    for EVENT in pygame.event.get():
        if EVENT.type == pygame.QUIT:
            exit()
        if EVENT.type == pygame.KEYDOWN:
            if EVENT.key == pygame.K_ESCAPE:
                exit()
    if SourceBranch.length <= CUTOFF:
        return 0
    else:
        if direction == 0:
            angle = randint(0,down)+SourceBranch.angle
        else:
            angle = randint(-1*down,0)+SourceBranch.angle
        #print(angle)
        root = SourceBranch.top
        newLength = SourceBranch.length*lengthDelta-constant
        #print(newLength)
        topx = round(math.cos(math.radians(angle))*newLength)+root[0]
        topy = round(math.sin(math.radians(angle))*newLength)+root[1]
        drawLine(root,(topx,topy),round(weight))
        top = (topx,topy)
        me = Branch(root,top,newLength,angle)
        splitCount = randint(2,maxSplits)
        for i in range(splitCount):
            makeBranch(me,i%2,max(1,weight-0.6))
if __main__ == "__main__":
    main()
