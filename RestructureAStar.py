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
		self.CurAdjacent = []
		self.SetPath()
		self.setHScore()
	
	def setHScore(self):
		for n in self.Nodes:
			n.SetHScore(10*(abs(n.GridPos[0] - self.Goal.GridPos[0]) + abs(n.GridPos[1] - self.Goal.GridPos[1])))
	
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
		if Node not in self.openList:
			self.openList.append(Node)
			self.CurAdjacent.append(Node)
		Node.Parent = self.currentNode
		Node.SetGScore(gValue)
		Node.SetFScore()
			
	def CheckChildren(self):
		if(self.openList.count > 0):
			self.openList.sort(key = lambda Node : Node.fScore)
			self.currentNode = self.openList[0]
			self.openList.remove(self.currentNode)
			self.closedList.append(self.currentNode)
			i = 0
			for adj in self.CurAdjacent:
				if adj not in self.openList:
					self.openList.append(adj)
					adj.Parent = self.currentNode
				else:
					move = 10 if i < 4 else 14
					movecost = move + self.currentNode.gScore
					if movecost < adj.gScore:
						adj.Parent = self.currentNode
						adj.SetGScore(movecost)
				i += 1
			self.GetAdjacent()
		
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