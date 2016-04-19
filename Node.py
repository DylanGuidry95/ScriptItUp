import pygame as gfx

class Node:	
	def __init__(self,xPos, yPos, Walkable):
		self.Walkable = Walkable
		self.Target = False
		self.Parent = None
		self.Color = (0,0,0)
		self.Width = 10
		self.Height = 10
		self.Margin = 10
		self.Left = (self.Margin + self.Width) * xPos + self.Margin
		self.Top = (self.Margin + self.Height) * yPos + self.Margin
		self.Pos = xPos, self.Height - yPos
		self.fScore = None
		self.gScore = None
		self.hScore = None
		
	def ChangeVisual(self, Color, Target):
		self.Color = Color
		self.Target = Target
		
	def DrawNode(self, screen, color):
		Margin = self.Margin

		if (self.Walkable and self.Target == False):
			color = (0,0,255) 
		elif (self.Target == False):
			color = (255,0,0)
		gfx.draw.rect(screen, color, (self.Left , self.Top, self.Width, self.Height))
		
	def GetFScore(self):
		return self.hScore + self.hScore
		
	def GetHScore(self, value):
		self.hScore = value
		
	def GetGScore(self, value):
		self.gScore = value