import pygame

class Node:
	xPos = 0
	yPos = 0
	
	hScore = 0
	gScore = 0
	fScore = gScore + hScore
	
	color = (255,0,0)
	
	def __init__(self,xPos, yPos, Name):
		self.xPos = xPos
		self.yPos = yPos
		self.Name = Name
		
	def SetParent(self, Parent):
		self.Parent = Parent
		
	def DrawNode():
		pygame.gfxdraw.filled_circle((255,255,255, self.xPos, self.yPos, 30, col))