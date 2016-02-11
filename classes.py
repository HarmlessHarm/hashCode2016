import math

class Product(object):
	"""docstring for Product"""
	def __init__(self, weight, pType):
		# super(Product, self).__init__()
		self.weight = weight
		self.pType = pType

class Warehouse(object):
	"""docstring for Warehouse"""
	def __init__(self, whID, x, y):
		# super(Warehouse, self).__init__()
		self.id = whID
		self.x = x
		self.y = y
		self.stock = {}

	def addStock(self, product):
		pType = product.pType
		if pType not in self.stock:
			self.stock[pType] = []
		self.stock[pType].append(product)

	def getCoords(self):
		return (self.x, self.y)
		
class Order(object):
	"""docstring for Order"""
	def __init__(self, orderID, destX, destY, pType):
		# super(Order, self).__init__()
		self.id = orderID
		self.destX = destX
		self.destY = destY
		self.pType = pType

	def getCoords(self):
		return (self.destX, self.destY)

class Drone(object):
	"""docstring for Drone"""
	def __init__(self, droneID, x, y):
		# super(Drone, self).__init__()
		self.id = droneID
		self.currentX = x
		self.currentY = y
		self.targetX = None
		self.targetY = None

	def updatePos(self):
		self.currentX = self.targetX
		self.currentY = self.targetY

	def setTarget(self, targetX, targetY):
		updatePos(self)
		self.targetX = targetX
		self.targetY = targetY
		dist = math.sqrt((startX - endX)**2 + (startY - endY)**2)
		self.timeToTarget = ceil(dist)

	def timeStep(self):
		self.timeToTarget -= 1
	

		