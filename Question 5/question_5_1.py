# I fail to find an alforithm to solve question 5.
# this method is only to solve L = odd number, two colors, but enough for Q5.1
import numpy as np

L = 5
R_num = 7
B_num = 18
llist = []

# penalty = 0
if R_num == int(L*L/2+1):
	for i in range(L*L):
		if i%2 == 0:
			llist.append('R')
		else:
			llist.append('B')

if B_num == int(L*L/2+1):
	for i in range(L*L):
		if i%2 == 0:
			llist.append('B')
		else:
			llist.append('R')

# penalty != 0
middle = int(L*L/2)
num = 0
lessColor = ''
mat = np.zeros(25,dtype=np.str) 

if R_num > B_num:
	mat[:] = 'R'
	lessColor = 'B'
	mat[middle] = 'B'
	num = B_num -1
else:
	mat[:] = 'B'
	lessColor = 'R'
	mat[middle] = 'R'
	num = R_num -1

# to minimum penalty, should find out not neighbors' color set as much as possible
# color			color 
#		color
# color   		color

# for R_num = 8, B_num = 17
# ['B', 'B', 'B', 'B', 'R'],
# ['B', 'R', 'B', 'R', 'B'],
# ['R', 'B', 'R', 'B', 'R'],
# ['B', 'R', 'B', 'R', 'B'],
# ['B', 'B', 'B', 'B', 'B']

for i in range(num):
	if num > 0:
		mat[middle-(2*i+2)] = lessColor
		num -= 1
	if num > 0:
		mat[middle+(2*i+2)] = lessColor
		num -= 1
mat.reshape(L,L)

