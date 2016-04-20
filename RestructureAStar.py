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
		
	def ParentNodes(self, Node , ParentNode):
		Node.IsChild(ParentNode)
		Node.IsChild(True)
		
	def SetPath(self):
		randA = randint(0, len(self.Nodes) - 1)
		randB = randint(0, len(self.Nodes) - 1)
		if(self.Nodes[randA].Walkable == False or self.Nodes[randB].Walkable == False):
			self.SetPath()
		else:
			self.Start = self.Nodes[randA]
			self.currentNode = self.Nodes[randA]
			self.Goal = self.Nodes[randB]
			self.openList.append(self.Start)
			self.Start.SetTarget(True)
			self.Goal.SetTarget(True)
	
	def Algorithm(self, width, height):
		if(self.IsGoal == True):
			self.SetPath()
		else:
			self.GetAdjacent()
				
	def GetAdjacent(self):
		for n in self.Nodes:
			if(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] and n.Walkable == True and (n not in self.closedList)): #Left
				n.SetGScore(10 + n.GetGScore())
				self.CheckNode(n,10)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] and n.Walkable == True and (n not in self.closedList)): #Right
				n.SetGScore(10 + n.GetGScore())
				self.CheckNode(n, 10)
			elif(n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.GridPos[0] == self.currentNode.GridPos[0] and n.Walkable == True and (n not in self.closedList)): #Top
				n.SetGScore(10 + n.GetGScore())
				self.CheckNode(n, 10)	
			elif(n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.GridPos[0] == self.currentNode.GridPos[0] and n.Walkable == True and (n not in self.closedList)): #Bottom
				n.SetGScore(10 + n.GetGScore())
				self.CheckNode(n, 10)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.Walkable == True and (n not in self.closedList)): #Top Right
				n.SetGScore(14 + n.GetGScore())
				self.CheckNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] + 1 and n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.Walkable == True and (n not in self.closedList)): #Bot Right
				n.SetGScore(14 + n.GetGScore())
				self.CheckNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] + 1 and n.Walkable == True and (n not in self.closedList)): #Top Left
				n.SetGScore(14 + n.GetGScore())
				self.CheckNode(n, 14)
			elif(n.GridPos[0] == self.currentNode.GridPos[0] - 1 and n.GridPos[1] == self.currentNode.GridPos[1] - 1 and n.Walkable == True and (n not in self.closedList)): #Bot Right
				n.SetGScore(14 + n.GetGScore())
				self.CheckNode(n, 14)
		
		self.FindLowestFScore()
			
	def CheckNode(self, Node, gValue):
		if Node not in self.openList:
			self.ParentNodes(Node, self.currentNode)
			self.openList.append(Node)
	
	def FindLowestFScore(self):
		self.GetManhattan()
		self.openList.remove(self.currentNode)
		self.openList.sort(key = lambda Node: Node.fScore)
		self.currentNode = self.openList[0]
		for n in self.openList:
			ngScore = n.GetGScore()
			cgScore = self.currentNode.GetGScore()
			if n != self.currentNode and ngScore <= cgScore:
				self.ParentNodes(self.currentNode, Node)
				self.currentNode = Node
			else:
				self.closedList.append(n)

	def GetManhattan(self):
		for n in self.openList:
			n.SetHScore(10*(abs(n.GridPos[0]-self.Goal.GridPos[0]) + abs(n.GridPos[1]-self.Goal.GridPos[1])))
			n.fScore = n.GetFScore()
		
	def IsGoal(self):
		if(self.Goal in self.openList):
			for n in self.Nodes:
				n.Target = False
				n.Retrace = False
				n.Path = False
				n.Paraented = False
			return True
		else:
			return False