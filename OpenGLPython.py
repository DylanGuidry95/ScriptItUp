import sys, pygame
from Node import Node
from AStar import AStar
pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)

Nodes = []

xMax = 10
yMax = 10

index = 0

for i in range(xMax):
	for j in range(yMax):
		if (i >= 4 and i <= 6) and (j <= 8 and j >= 5):
			n = Node(i, j, False)
		else:
			n = Node(i, j, True)
		Nodes.append(n)
		index+=1
	
Algorithm  = AStar(Nodes)
Algorithm.DoAlgorithm(xMax,yMax)
Algorithm.Start.ChangeVisual((0,255,0), True)
Algorithm.Goal.ChangeVisual((0,255,0), True)

print Nodes[0].Color

print Algorithm.Start.Pos, Algorithm.Goal.Pos
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	for i in Nodes:
		i.DrawNode(screen, (255,255,255))
	
	
	pygame.display.flip()
	pygame.display.flip()