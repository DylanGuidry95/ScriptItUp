class AStar:
	def __init__(self, Nodes, w, h):
		self.Nodes = Nodes
		self.Start = None
		self.Goal = None
		self.openList = []
		self.closedList = []
		self.currentNode = None
		self.width = w
		self.height = h
		self.Begin()
		
	def Begin(self):
		self.Start = self.Nodes[8]
		self.Goal = self.Nodes[32]
		self.currentNode = self.Start
		self.openList.append(self.currentNode)
		self.Start.IsPath(True)
		self.Goal.IsPath(True)
		self.FindAdj()
		
	def FindAdj(self):
		if self.currentNode.AdjNodes:
			self.currentNode.AdjNodes = []
		index = self.Nodes.index(self.currentNode)
		bot = index + 1
		top = index - 1
		right = index + self.width
		left = index - self.width
		topLeft = left - 1
		topRight = right - 1
		botLeft = left + 1
		botRight = right + 1
		adjs = [bot, top, left, right, topLeft, topRight, botLeft, botRight]
		for i in adjs:
			if i in self.Nodes:
				if self.Nodes[i].walkable:
					self.currentNode.AdjNodes.append(self.Nodes[i])
		self.CheckAdj()
					
	def CheckAdj(self):
		while self.openList.count > 0:		
			print "hit"
			self.openList.sort(key = lambda x : x.fScore)
			self.currentNode = self.openList[0]
			if self.Goal in self.openList:
				break
	
			self.openList.remove(self.currentNode)			
			self.closedList.append(self.currentNode)
			i = 0			
			for adj in self.currentNode.AdjNodes:
				if adj.walkable and adj not in self.closedList:
					if adj not in self.openList:
						self.openList.append(adj)
						adj.Parent = self.currentNode						
						adj.g = 10 if i < 4 else 14
						
					else:
						move = 10 if i < 4 else 14
						movecost = move + self.current.gScore
						if movecost < adj.gScore: 
							adj.IsChild(self.currentNode)						
							adj.g = movecost
				i+=1
			self.FindAdj()
		