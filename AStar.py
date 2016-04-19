from Node import Node
from random import randint
import time

class AStar:
	def __init__(self, Nodes):
		self.Start = None
		self.Goal = None
		self.Nodes = Nodes
		self.openList = []
		self.closedList = []
		self.currentNode = None
		self.Fail = False
		self.Adjacent = []
		
	def Parent(self, Node):
		if Node.GridPos != self.currentNode.GridPos:
			Node.SetParent(self.currentNode)
			Node.ShowParented(True)
		
	def SetPath(self):
		randA = randint(0, len(self.Nodes) - 1)
		randB = randint(0, len(self.Nodes) - 1)
		if(self.Nodes[randA].Walkable == False or self.Nodes[randB].Walkable == False):
			self.SetPath()
		else:
			self.Start = self.Nodes[randA]
			self.Goal = self.Nodes[randB]
			self.openList.append(self.Start)
			self.Start.SetTarget(True)
			self.Goal.SetTarget(True)
	
	def DoAlgorithm(self,width, height):
		self.SetPath()		
		self.currentNode = self.Start
		self.GetAdjacent(self.currentNode)
		self.CheckPath()
			
	def CheckPath(self):
		if self.Start in self.openList:
			self.openList.remove(self.Start)
			self.closedList.append(self.Start)
			
		self.GetManhattan()
		
		self.openList.sort(key = lambda Node: Node.fScore)
		
		if(self.openList != []):
			self.currentNode = self.openList[0]
		else:
			self.Fail = True
						
		self.openList.remove(self.currentNode)
		self.closedList.append(self.currentNode)
		self.currentNode.IsPath(True)	
	
	def GetAdjacent(self, Location):
		self.adjacent = []
		Fail = False
		for n in self.Nodes:
			if(n.GridPos[0] == Location.GridPos[0] + 1 and n.GridPos[1] == Location.GridPos[1] and n.Walkable == True): #Left
				n.SetGScore(10)
				self.Parent(n)
				self.openList.append(n)
			elif(n.GridPos[0] == Location.GridPos[0] - 1 and n.GridPos[1] == Location.GridPos[1] and n.Walkable == True): #Right
				n.SetGScore(10)
				self.Parent(n)
				self.openList.append(n)	
			elif(n.GridPos[1] == Location.GridPos[1] + 1 and n.GridPos[0] == Location.GridPos[0] and n.Walkable == True): #Top
				n.SetGScore(10)
				self.Parent(n)
				self.openList.append(n)	
			elif(n.GridPos[1] == Location.GridPos[1] - 1 and n.GridPos[0] == Location.GridPos[0] and n.Walkable == True): #Bottom
				n.SetGScore(10)
				self.Parent(n)
				self.openList.append(n)
			elif(n.GridPos[0] == Location.GridPos[0] + 1 and n.GridPos[1] == Location.GridPos[1] + 1 and n.Walkable == True): #Top Right
				n.SetGScore(14)
				self.Parent(n)
				self.openList.append(n)
			elif(n.GridPos[0] == Location.GridPos[0] + 1 and n.GridPos[1] == Location.GridPos[1] - 1 and n.Walkable == True): #Bot Right
				n.SetGScore(14)
				self.Parent(n)
				self.openList.append(n)
			elif(n.GridPos[0] == Location.GridPos[0] - 1 and n.GridPos[1] == Location.GridPos[1] + 1 and n.Walkable == True): #Top Left
				n.SetGScore(14)
				self.Parent(n)
				self.openList.append(n)
			elif(n.GridPos[0] == Location.GridPos[0] - 1 and n.GridPos[1] == Location.GridPos[1] - 1 and n.Walkable == True): #Bot Right
				n.SetGScore(14)
				self.Parent(n)
				self.openList.append(n)
			
	
	def GetManhattan(self):
		for n in self.openList:
			n.SetHScore(10*(abs(n.GridPos[0]-self.Goal.GridPos[0]) + abs(n.GridPos[1]-self.Goal.GridPos[1])))
			n.fScore = n.GetFScore()
	
	def CheckCompletion(self):
		if(self.currentNode.GridPos == self.Goal.GridPos):
			for n in self.Nodes:
				n.Target = False
				n.Retrace = False
				n.Path = False
				n.Paraented = False
			return True
		else:
			return False
		
		
		
