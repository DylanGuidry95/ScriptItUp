import pygame as gfx

class Node:	
	def __init__(self,xPos, yPos, Walkable):
		self.Walkable = Walkable
		self.Target = False
		self.Paraented = False
		self.Parent = None
		self.Color = (0,0,0)
		self.Width = 10
		self.Height = 10
		self.Margin = 10
		self.Left = (self.Margin + self.Width) * xPos + self.Margin
		self.Top = (self.Margin + self.Height) * yPos + self.Margin
		self.WorldPos = xPos, self.Height - yPos
		self.GridPos = [xPos, yPos]
		self.fScore = 0
		self.gScore = 0
		self.hScore = 0
		self.Path = (0,0,0)
		self.Retrace = False
		self.Child = False
		
	def SetTarget(self,Target):
		self.Target = Target
		
	def IsPath(self, Path):
		self.Path = Path
		
	def IsRetrace(self, Retrace):
		self.Retrace = Retrace
	
	def DrawNode(self, screen, color):
		Margin = self.Margin
		if (self.Walkable == True):
			color = (0,0,255) 
		if (self.Walkable == False):
			color = (255,0,0)
		if (self.Child == True):
			color = (0,255,0)
		if (self.Target == True):
			color = (255,255,255)
		if (self.Path == True):
			color = (255, 0, 255)
		if (self.Retrace == True):
			color = (0, 0, 0)
		gfx.draw.rect(screen, color, (self.Left , self.Top, self.Width, self.Height))
		
	def GetFScore(self):
		return self.fScore
		
	def SetFScore(self):
		self.fScore = self.hScore + self.gScore
		return self.fScore
		
	def SetHScore(self, value):
		self.hScore = value
		
	def SetGScore(self, value):
		self.gScore = value
	
	def GetGScore(self):
		return self.gScore
	
	def IsChild(self, Node):
		self.Parent = Node
		self.Child = True
		
	def GetGScore(self):
		return self.gScore