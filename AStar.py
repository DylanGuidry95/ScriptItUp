from Node import Node

class AStar:
	def __init__(self, Nodes):
		self.Start = None
		self.Goal = None
		self.Nodes = Nodes
		self.openList = []
		
	def DoAlgorithm(self,width, height):
		startIndex = 0
		self.Start = self.Nodes[0]
		self.Goal = self.Nodes[33]
		self.openList.append(self.Nodes[startIndex])
		for i in range(0,8):
			if(startIndex - 1 > 0):
				self.openList.append(self.Nodes[startIndex - 1])
				print self.Nodes[startIndex - 1].Pos
			if(startIndex + 1 < width):
				self.openList.append(self.Nodes[startIndex + 1])
				print self.Nodes[startIndex + 1].Pos
			if(startIndex - width > 0):
				self.openList.append(self.Nodes[startIndex - width])
				print self.Nodes[startIndex - width].Pos
				if(startIndex - width + 1 < width):
					self.openList.append(self.Nodes[startIndex - width + 1])
					print self.Nodes[startIndex - width + 1].Pos
				if(startIndex - width + 1 < width):
					self.openList.append(self.Nodes[startIndex - width - 1])
					print self.Nodes[startIndex - width - 1].Pos
			if(startIndex + width < height):
				self.openList.append(self.Nodes[startIndex + width])
				print self.Nodes[startIndex + width].Pos
				if(startIndex + width + 1 < width):
					self.openList.append(self.Nodes[startIndex + width + 1])
					print self.Nodes[startIndex + width + 1].Pos
				if(startIndex + width - 1 > 0):
					self.openList.append(self.Nodes[startIndex + width - 1])
					print self.Nodes[startIndex + width - 1].Pos
				
		for n in self.openList:
			if(n != self.Start):
				n.SetParent(self.Start)
				print n.Pos
				
		self.openList.remove(self.Nodes[0])
		
