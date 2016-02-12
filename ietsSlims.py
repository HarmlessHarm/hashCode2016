import classes, math, random
import HashCode2016 as hc

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

	dataDict['warehouses'].append(classes.Warehouse(1,8,8))
	
	for product in dataDict['products']:
		warehouse = dataDict['warehouses'][int(round(random.random()))]
		warehouse.addStock(product)
	for wh in dataDict['warehouses']:
		print wh.stock
	dataDict['orders'].append(classes.Order(0,3,6,0))
	dataDict['orders'].append(classes.Order(1,7,2,0))
	dataDict['orders'].append(classes.Order(2,1,8,1))
	dataDict['orders'].append(classes.Order(3,6,6,1))
	dataDict['orders'].append(classes.Order(4,5,9,0))
	dataDict['orders'].append(classes.Order(5,7,2,0))
	dataDict['orders'].append(classes.Order(6,7,8,1))
	dataDict['orders'].append(classes.Order(7,10,10,1))
	wareh = dataDict['warehouses'][0]
	for i in range(dataDict['dronesN']):

		dataDict['drones'].append(classes.Drone(0, wareh.x, wareh.y))

	return dataDict

def getWh(order, warehouses):
	bestScore = 9999999999
	for wh in warehouses:
		if order.pType in wh.stock:
			dist = getDist(order.getCoords(), wh.getCoords())
			if dist < bestScore:
				bestScore = dist
				bestW = wh
	return bestW
			
def getDist((startX, startY), (endX, endY)):
	dist = math.sqrt((startX - endX)**2 + (startY - endY)**2)
	return dist


def orderDrones(data):
	warehouses = data['warehouses']
	drone = data['drones'][0].id
	printList = []
	for order in data['orders']:

		warehouse = getWh(order, warehouses)
		printList.append(str(drone)+"L"+str(warehouse.id)+str(order.pType)+"1")
		printList.append(str(drone)+"D"+str(order.id)+str(order.pType)+"1")
	with open("output.out", 'w') as writeFile:
		for line in printList:
			writeFile.write(line+"\n")


data = hc.main()
# data = createData()

orderDrones(data)