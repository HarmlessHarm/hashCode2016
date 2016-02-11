class Product(object):
	"""docstring for Product"""
	def __init__(self, weight, pType):
		# super(Product, self).__init__()
		self.weight = weight
		self.pType = pType

class Warehouse(object):
	"""docstring for Warehouse"""
	def __init__(self, x, y):
		# super(Warehouse, self).__init__()
		self.x = x
		self.y = y
		self.stock = {}

	def addStock(self, product):
		pType = product.pType
		if pType not in stock:
			self.stock[pType] = []
		self.stock[pType].append(product)

		
class Order(object):
	"""docstring for Order"""
	def __init__(self, destX, destY, pType):
		# super(Order, self).__init__()
		self.destX = destX
		self.destY = destY
		self.pType = pType

class Drone(object):
	"""docstring for Drone"""
	def __init__(self):
		# super(Drone, self).__init__()
		# self.arg = arg

	def updatePos(self):
		self.currentX = self.targetX
		self.currentY = self.targetY

	def updateTarget(self, targetX, targetY):
		self.targetX = targetX
		self.targetY = targetY

	def setTimeToTarget(self, time):
		self.timeToTarget = time
		
		