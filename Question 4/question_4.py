# here I use "two pass" algorithem and do 4-connectivity check
import numpy as np

mat = [[0,0,0,0,1,1,0,0,0,1,0,1,0,1,1,1,0,0,1,1],
		[1,0,1,0,0,0,0,0,1,1,0,0,0,0,1,0,0,1,0,0],
		[0,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0],
		[0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,1],
		[1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1],
		[1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1],
		[1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,0,1,0,1],
		[0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
		[0,0,1,1,1,0,0,1,0,1,0,0,1,0,0,0,1,1,1,0],
		[1,0,1,0,1,0,1,1,1,1,0,0,1,0,1,0,0,0,0,1],]

def twoPass(mat):
	row, col = mat.shape
	label = 0

	# first pass, 4-connectivity check
	for x in range(row):
		for y in range(col):
			if mat[x, y] == 0:
				continue
			if mat[x,y] == 1:
				# first row and col, if left/up is 0, assign +1 label
				if x == 0:
					if mat[0,y-1] == 0:
						label += 1
						mat[x,y] = label
					elif mat[0,y-1] != 0:
						mat[x,y] = label
				elif y == 0:
					if mat[x-1,0] == 0:
						label += 1
						mat[x,y] = label		
					elif mat[x-1,0] != 0:
						mat[x,y] = label
				# if neighbors are both 0,assign +1 label
				elif mat[x-1,y] == 0 and mat[x,y-1] == 0:
					label += 1
					mat[x,y] = label
				# if left/up has 1, assign the minimum one, except 0
				elif mat[x-1,y] > 1 or mat[x,y-1] > 1:
					if mat[x-1,y] == 0:
						mat[x,y] = mat[x,y-1]
					elif mat[x,y-1] == 0:
						mat[x,y] = mat[x-1,y]					
					else: 
						mat[x,y] = min(mat[x-1,y],mat[x,y-1])
	# print(mat)
	
	# create a neighbor matrix, to indicate the relationship of left/up label
	neighbors = np.zeros((label, label), dtype=np.int8)
	for x in range(row):
		for y in range(col):
			if mat[x, y] >= 1:
				flag = True
				#  label itself in the matrix
				if mat[x-1,y] == 0 and mat[x,y-1] == 0:
					neighbors[mat[x,y]-1, mat[x,y]-1] = 1	
					flag = False
				# first row and col
				if x == 0 or y == 0:
					neighbors[mat[max(0,x-1),y]-1, mat[x,y]-1] = 1
					neighbors[mat[x,y]-1, mat[max(0,x-1),y]-1] = 1
					flag = False	
				# label the neighbor relationship in the matrix
				if mat[x-1,y] > 0 and flag:
					neighbors[mat[x-1,y]-1, mat[x,y]-1] = 1
					neighbors[mat[x,y]-1, mat[x-1,y]-1] = 1
				if mat[x,y-1] > 0 and flag:
					neighbors[mat[x,y-1]-1, mat[x,y]-1] = 1
					neighbors[mat[x,y]-1, mat[x,y-1]-1] = 1
	# print(neighbors)

	# to find out the minimum neighbor index of each label
	minLabel = list(np.zeros(label, dtype=np.int8))
	for i in range(label):
		l = []
		for j in range(label):
			if neighbors[i, j] == 1:
				l.append(j+1)
		minLabel[i] = min(l)
	for i in range(len(minLabel)):
		for j in range(len(minLabel)):
			if minLabel[j] > minLabel[minLabel[i]-1]:
				minLabel[i] = minLabel[minLabel[i]-1]
	# print(minLabel)

	# second pass
	for x in range(row):
		for y in range(col):
			if mat[x,y] > 1:
				mat[x,y] = minLabel[mat[x,y]-1]
	return mat

mat = twoPass(mat = np.array(mat))
print(str(mat).replace(']','\n').replace('[','').replace(',',''))

# f = open('output_question_4','w')
# for i in range(mat.shape[0]):
# 	for j in range(mat.shape[1]):
# 		sstring = ''
# 		sstring = str(mat[i][j])
# 		f.write(sstring)
# 		f.write(' ')
# 	f.write('\n')
# f.close()