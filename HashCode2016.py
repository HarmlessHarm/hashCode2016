import classes

# Given info
parameters = {}
productsInfo = {}
ordersInfo = {}

# warehouses
nWarehouses = 0
warehouses = []
coordinates = []
nItemsOfProduct = []

# Per order
orderCoords = []
orderNItems = []
itemsOfType = []

def main():
    readFile("./input/mother_of_all_warehouses.in")

    print(parameters)
    print(productsInfo)
    print(warehousesInfo)
    print(ordersInfo)

    # warehouses
    # print(warehouses)
    # print(coordinates)
    # print(nItemsOfProduct)
    #
    # # Per order
    # print(orderCoords)
    # print(orderNItems)
    # print(itemsOfType)

def readFile(inputfile):
    # import file
    global nWarehouses
    whid = 0
    with open(inputfile, 'r') as rf:
        # read file lines
        for i, line in enumerate(rf):
            # read parameters line
            if i == 0:
                getParameters(line)

            # Get products
            if i == 1:
                productsInfo["nTypes"] = int(line)
            elif i == 2:
                productsInfo["weights"] =  [int(n) for n in line.split()]

            # Warehouses
            if i == 3:
                nWarehouses = int(line)
            if i > 3 and i <= 3 + (nWarehouses * 2):
                # get coordinate\

                if i % 2 == 0:
                    lineList = line.split()
                    # coords = ()
                    warehouse = classes.Warehouse(int(lineList[0]), int(lineList[1]))
                    whid += 1
                    warehouses.append(warehouse)
                    # coordinates.append(coords)
                else:
                    for i, n in enumerate(line.split()):
                        for j in range(int(n)):
                            newProduct = classes.Product(productInfo['weights'][i], i)
                            warehouses[-1].addStock(newProduct)
                    # nItemsOfProduct = [int(n) for n in line.split()]
                print warehouses[0].x, warehouses[0].y
            # Orders
            if i == (3 + nWarehouses * 2) + 1:
                ordersInfo["nOrders"] = int(line)

            if i > (3 + nWarehouses * 2) + 1 and \
                i <= ( (3 + nWarehouses * 2) + 1) + ordersInfo["nOrders"] * 2:
                # get destination coordinate
                if i % 3 == 0:
                    lineList = line.split()
                    coords = (int(lineList[0]), int(lineList[1]))
                    orderCoords.append(coords)
                # get number of items
                elif i % 3 == 1:
                    orderItems.append(int(line))
                # get number of items per type
                elif i % 3 == 2:
                    itemsOfType = [int(n) for n in line.split()]


# def makeWarehouses():
#     for i in range(warehousesInfo["nWarehouses"]):
#         # warehouseCoord =
#         warehouses.append(Warehouse())

# def getWarehouseInfo(line):
#     warehousesInfo["warehouseWeights"] = [int(n) for n in line.split()]


def getParameters(line):
    line = line.split()
    parameters["dimension"] = (int(line[0]), int(line[1]))
    parameters["nDrones"] = int(line[2])
    parameters["maxTime"] = int(line[3])
    parameters["maxPayload"] = int(line[4])

if __name__ == '__main__':
    main()
