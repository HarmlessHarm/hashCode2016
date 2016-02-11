import classes

def createData():
	dataDict = {
		'dimensions' : (10,10),
		'dronesN': 1,
		'time' : 1000,
		'payload' : 500,
		'drones' : [],
		'products' : [],
		'warehouses' : [],
		'orders' : []
	}
	for i in range(5):
		dataDict['products'].append(classes.Product(100, 0))
		dataDict['products'].append(classes.Product(50, 1))

	dataDict['warehouses'].append(classes.Warehouse(0,4,5))

	dataDict['warehouses'].append(classes.Warehouse(1,4,5))
	
	for product in dataDict['products']:
		warehouse = dataDict['warehouses'][product.pType]
		warehouse.addStock(product)
	# for wh in dataDict['warehouses']:
	# 	print wh.stock
	dataDict['orders'].append(classes.Order(0,3,6,0))
	dataDict['orders'].append(classes.Order(1,7,2,0))
	dataDict['orders'].append(classes.Order(2,1,8,1))
	dataDict['orders'].append(classes.Order(3,6,6,1))
	wareh = dataDict['warehouses'][0]
	for i in range(dataDict['dronesN']):

		dataDict['drones'].append(classes.Drone(0, wareh.x, wareh.y))

	return dataDict

def orderDrones(data):
	warehouse = data['warehouses'][0].id
	drone = data['drones'][0].id
	for order in data['orders']:
		
		print str(drone)+"L"+str(warehouse)+str(order.pType)+"1"
		print str(drone)+"D"+str(order.id)+str(order.pType)+"1"

data = createData()

orderDrones(data)