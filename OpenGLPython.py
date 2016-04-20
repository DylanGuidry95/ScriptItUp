import sys, pygame
from Node import Node
from AStar import AStar
from random import randint
import time
from RestructureAStar import RestructureAStar

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

Nodes = []

xMax = 7
yMax = 6

for x in range(0,xMax):
	for y in range(0,yMax):
		if x == 3 and (y == 1 or y == 2 or y == 3):
			n = Node(x,y,False)
		else:
			n = Node(x,y,True)
		Nodes.append(n)
	
Algorithm  = RestructureAStar(Nodes)


initialStart = True


	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	if(Algorithm.IsComplete() == False):
		Algorithm.GetAdjacent()
		
	for i in Nodes:
		i.DrawNode(screen, (255,255,255))
	
	
	pygame.display.flip()
	pygame.display.flip()