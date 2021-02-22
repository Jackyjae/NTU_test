L1 = 50
L2 = 57

inputCoordinatesFile = 'input_coordinates_7_1.txt'
inputIndexFile = 'input_index_7_1.txt'
outputIndexFile = 'output_index_7_1.txt'
outputCoordinatesFile = 'output_coordinates_7_1.txt'

# find index
coordinates = []
I = []
# read inputCoordinates
inputCoordinates = open(inputCoordinatesFile) 
lines = inputCoordinates.readlines()[1:]
for line in lines:
		coordinates.append(int(line.split()[0]))
		coordinates.append(int(line.split()[1]))
inputCoordinates.close()
# I = x1 + L1 * x2
for i in range(int(len(coordinates) / 2)):
	I.append(coordinates[2*i] + L1 * coordinates[2*i+1])
# output index
f = open(outputIndexFile,'w')
f.write('index')
# print('index')
for i in range(len(I)):
	# print(I[i])
	sstring = ''
	sstring = str(I[i])
	sstring = '\n' + sstring
	f.write(sstring)
f.close()

# find coordinates
x1 = []
x2 = []
I = []
# read inputIndex
inputIndex = open(inputIndexFile) 
lines = inputIndex.readlines()[1:]
for line in lines:
		I.append(int(line))
inputIndex.close()
# x1 = I%L1
# x2 = int(I/L1)
for i in range(len(I)):
	x1.append(I[i] % L1)
	x2.append(int(I[i] / L1))
# output coordinates
f = open(outputCoordinatesFile,'w')
f.write('x1 x2')
# print('x1 x2')
for i in range(len(x1)):
	# print(x1[i], x2[i])
	sstring = ''
	sstring = '\n'+str(x1[i])+' '+str(x2[i])
	f.write(sstring)
f.close()