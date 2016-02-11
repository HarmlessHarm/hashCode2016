

def readFile(fileName):

	data = []
	with open(fileName, 'r') as rf:
		for line in rf:
			data.append(line)
	return data

def writeFile(fileName, data):

	with open(fileName, 'w') as wf:
		for entry in data:
			wf.write(entry)
			wf.write("\n")