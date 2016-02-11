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
		self.stock = []

	def addStock(self, product):
		
		
		