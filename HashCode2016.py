import classes

parameters = {}
productsInfo = {}
warehousesInfo = {}

def main():
    readFile("./input/mother_of_all_warehouses.in")

def readFile(inputfile):
    # import file
    with open(inputfile, 'r') as rf:
        # read file lines
        for i, line in enumerate(rf):

            # read parameters line
            if i == 0:
                getParameters(line)

            # get products
            if i == 1:
                productsInfo["nTypes"] = int(line)
            if i == 2:
                productsInfo["weights"] =  [int(n) for n in line.split()]

            # warehouses
            if i == 3:
                warehousesInfo["nWarehouses"] = int(line)


            if i > 3 and i <= (3 + warehousesInfo["nWarehouses"] * 2):
                print i
                # get coordinate
                if i % 2 == 0:
                    getWarehouseInfo(line)
                else:
                    print i
                    # n of items per product type

def getWarehouseInfo(line):
    warehousesInfo["warehouseWeights"] = [int(n) for n in line.split()]


def getParameters(line):
    line = line.split()
    parameters["dimension"] = (int(line[0]), int(line[1]))
    parameters["nDrones"] = int(line[2])
    parameters["maxTime"] = int(line[3])
    parameters["maxPayload"] = int(line[4])

if __name__ == '__main__':
    main()
