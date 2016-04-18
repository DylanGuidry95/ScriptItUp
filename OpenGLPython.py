import sys, pygame
from Node import Node
pygame.init()

size = width, height = 500, 500
speed = [2,2]
black = 0,0,0
BLUE =  (  0,   0, 255)
screen = pygame.display.set_mode(size)

Nodes = []

xMax = 3
yMax = 3

index = 0

for i in range(0,xMax):
	for j in range (0,yMax):
		n = Node(i, j, "Node" + str(index))
		Nodes.append(n)
		index+=1

		
#for i in range(0,len(Nodes)):
#	if i % xMax != xMax-1:
#		Nodes[i].SetParent(Nodes[i+1])
#	if (i % xMax) != (xMax - 1) and (i % xMax) != (xMax - 2):
#		Nodes[i].SetParent(Nodes[i + 2])
		
#	if i < (xMax * yMax) - xMax:
#		Nodes[i].SetParent(Nodes[i + xMax])
#	if i < (xMax * yMax) - xMax * 2:
#		Nodes[i].SetParent(NODES[i + xMax])
		
#	print Nodes[i].Name, Nodes[i].Parent.Name
	
	
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	
	for i in Nodes:
		pygame.draw.circle(screen, BLUE, [i.xPos, i.yPos], 5, 0)
	
	screen.fill(black)
	pygame.display.flip()