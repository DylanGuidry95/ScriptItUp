from Node import Node
from random import randint
import time

class RestructureAStar:
	def __init__(self, Nodes):
		self.Start = None
		self.Goal = None
		self.Nodes = Nodes
		self.openList = []
		self.closedList = []
		self.currentNode = None
		self.Fail = False
		self.Adjacent = []
		self.SetPath()
		
	def SetPath(self):
		for n in self.Nodes:
			if n.GridPos == [1,2]:
				self.Start = n
				self.Start.SetTarget(True)
				self.currentNode = self.Start
				self.openList.append(self.currentNode)
			if n.GridPos == [5,2]:
				self.Goal = n
				self.Goal.SetTarget(True)
		self.GetAdjacent()
		
	def AddNode(self, Node, gValue):
		if(Node not in self.openList):
			Node.SetGScore(10 + self.currentNode.GetGScore())
			self.openList.append(Node)
			Node.IsChild(self.currentNode)
			self.currentNode.IsPath(True)
			self.currentNode.SetHScore(10*(abs(Node.GridPos[0]-self.Goal.GridPos[0]) + abs(Node.GridPos[1]-self.Goal.GridPos[1])))
			self.currentNode.SetFScore()
		else:
			if(Node.GetGScore() < self.GetGScore() + gValue):
				self.openList.remove(self.currentNode)
				self.closedList.append(self.currentNode)
				self.currentNode = Node
				self.openList.append(currentNode)
			
	def CheckChildren(self):
		if(self.openList.count > 0):
			for n in self.openList:
				self.currentNode = n
				if(n.SetFScore() < self.currentNode.SetFScore()):
					self.closedList.append(self.currentNode)
					self.currentNode = n
					self.openList.append(n)
				else: 
					self.closedList.append(n)
			
			self.currentNode.IsPath(True)
		else:
			print "No Path"
		
	def IsComplete(self):
		if(self.Goal not in self.openList):
			return False
		else:
			return True
		
	def GetAdjacent(self):
		for n in self.Nodes:
			if(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] and n.Walkable == True and (n not in self.closedList)): #Left
				self.AddNode(n,10)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] and n.Walkable == True and (n not in self.closedList)): #Right
				self.AddNode(n, 10)
			elif(n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.GridPos[0] == self.currentNode.GridPos[0] and n.Walkable == True and (n not in self.closedList)): #Top
				self.AddNode(n, 10)	
			elif(n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.GridPos[0] == self.currentNode.GridPos[0] and n.Walkable == True and (n not in self.closedList)): #Bottom
				self.AddNode(n, 10)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.Walkable == True and (n not in self.closedList)): #Top Right
				self.AddNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.Walkable == True and (n not in self.closedList)): #Bot Right
				self.AddNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.Walkable == True and (n not in self.closedList)): #Top Left
				self.AddNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.Walkable == True and (n not in self.closedList)): #Bot Right
				self.AddNode(n, 14)
		self.CheckChildren()