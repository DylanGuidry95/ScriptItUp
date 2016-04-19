import sys, pygame
from Node import Node
from AStar import AStar
from random import randint
import time

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

Nodes = []

for x in range(0,10):
	for y in range(0,10):
		if (randint(0,10) >= 7):
			n = Node(x, y, False)
		else:
			n = Node(x, y, True)
		Nodes.append(n)
	
Algorithm  = AStar(Nodes)


initialStart = True

for n in Algorithm.openList:
	n.ShowParented(True)
	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	if(initialStart == True):
		Algorithm.DoAlgorithm(10,10)
		initialStart = False
	
	if(Algorithm.CheckCompletion() == True or Algorithm.Fail == True):
		time.sleep(2.5)
		Algorithm.DoAlgorithm(10, 10)
		
	elif Algorithm.CheckCompletion() == False:
		time.sleep(.2)
		Algorithm.GetAdjacent(Algorithm.currentNode)
		Algorithm.CheckPath()
		
	for i in Nodes:
		i.DrawNode(screen, (255,255,255))
	
	
	pygame.display.flip()
	pygame.display.flip()