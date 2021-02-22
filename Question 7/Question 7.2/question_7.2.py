L1 = 4
L2 = 8
L3 = 5
L4 = 9
L5 = 6
L6 = 7

inputCoordinatesFile = 'input_coordinates_7_2.txt'
inputIndexFile = 'input_index_7_2.txt'
outputIndexFile = 'output_index_7_2.txt'
outputCoordinatesFile = 'output_coordinates_7_2.txt'

# find index
coordinates = []
I = []
# read inputCoordinates
inputCoordinates = open(inputCoordinatesFile) 
lines = inputCoordinates.readlines()[1:]
for line in lines:
	for i in range(6):
		coordinates.append(int(line.split()[i]))
inputCoordinates.close()

# I = x1 + x2 * L1 + x3 * L1 * L2...
for i in range(int(len(coordinates) / 6)):
	I.append(coordinates[6*i] 
		+ coordinates[6*i+1] * L1
		+ coordinates[6*i+2] * L1*L2
		+ coordinates[6*i+3] * L1*L2*L3
		+ coordinates[6*i+4] * L1*L2*L3*L4
		+ coordinates[6*i+5] * L1*L2*L3*L4*L5)
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
x3 = []
x4 = []
x5 = []
x6 = []
I = []
# read inputIndex
inputIndex = open(inputIndexFile) 
lines = inputIndex.readlines()[1:]
for line in lines:
		I.append(int(line))
inputIndex.close()
# x1 = I%(L1*L2)%L1
# x2 = int(I%(L1*L2)/L1)
# x3 = int(I%(L1*L2*L3)/(L1*L2)...
for i in range(len(I)):
	x1.append(I[i]%(L1*L2)%L1)
	x2.append(int(I[i]%(L1*L2)/L1))
	x3.append(int(I[i]%(L1*L2*L3)/(L1*L2)))
	x4.append(int(I[i]%(L1*L2*L3*L4)/(L1*L2*L3)))
	x5.append(int(I[i]%(L1*L2*L3*L4*L5)/(L1*L2*L3*L4)))
	x6.append(int(I[i]%(L1*L2*L3*L4*L5*L6)/(L1*L2*L3*L4*L5)))
# output coordinates
f = open(outputCoordinatesFile,'w')
f.write('x1 x2 x3 x4 x5 x6')
# print('x1 x2 x3 x4 x5 x6')
for i in range(len(x1)):
	# print(x1[i], x2[i], x3[i], 
	# 	x4[i], x5[i], x6[i])
	sstring = ''
	sstring = '\n'+str(x1[i])+' '+str(x2[i])+' '+str(x3[i])+' '+str(x4[i])+' '+str(x5[i])+' '+str(x6[i])
	f.write(sstring)
f.close()