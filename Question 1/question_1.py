# For m*n matric, the maximum summary is the route from going down to the left bottom then go to the right bottom.
# And the subtracted value of the maximum summary and the summary given by the question can be considered as the account of the number/figure in the matric (from left bottom).
# So I change this question to find out how many "blocks" should be subtracted from the matric and the contour of the rest matric is the answer. Here's one of the routes.
import numpy as np

def findPath(row, col, summedNum):
	max_route_sum = sum(np.arange(row+1)) + row*(col-1)
	min_route_sum = (col-1) + sum(np.arange(row+1))
	# summed number is not in the range
	if summedNum < min_route_sum or summedNum > max_route_sum:
		print("summed number should be from", min_route_sum,"to", max_route_sum)
		return -1
	else:
		route_temp_row = ['D']*(row-1)
		route_temp_col = ['R']*(col-1)
		route = route_temp_row+route_temp_col
		# the substraction is refer to the amount of excluded number in the left bottom
		max_sub_summed = max_route_sum - summedNum

		quotient = int(max_sub_summed/(row-1))
		remainder = max_sub_summed%(row-1)

		sstring = ''
		
		if quotient == 0:
			# go right at first, quotient strides
			route[quotient+(row-1)-remainder] = 'R'
			# turn down then go right
			llist = ['D']*remainder
			route[quotient+(row-1)-remainder+1:+quotient+(row-1)+1] = llist
			print(summedNum, sstring.join(route))

		elif remainder == 0:
			# go down first, then turn tight then turn down
			llist = ['R']*quotient
			route[0:quotient] = llist
			# turn right
			llist = ['D']*(row-1-remainder)
			route[quotient:quotient+(row-1)-remainder] = llist
			print(summedNum, sstring.join(route))

		else:
			# go right at first, quotient strides
			llist = ['R']*quotient
			route[0:quotient] = llist
			# turn down, (m-1-remainder) strides
			llist = ['D']*(row-1-remainder)
			route[quotient:quotient+(row-1)-remainder] = llist
			# turn right 
			route[quotient+(row-1)-remainder] = 'R'
			# turn down again
			llist = ['D']*remainder
			route[quotient+(row-1)-remainder+1:+quotient+(row-1)+1] = llist
			print(summedNum, sstring.join(route))
		return route

# summary verification:
def sumVerification(route):
	num = 1
	add_num = 1
	for i in range(len(route)):
		if route[i] == 'R':
			num += add_num
		if route[i] == 'D':
			add_num += 1
			num += add_num
	print(num)

# I didn't notice thet I need to write the result into output file
# so I just saved the result from the terminal manually
findPath(9, 9, 65)
findPath(9, 9, 72)
findPath(9, 9, 90)
findPath(9, 9, 110)
print()
findPath(90000, 900000, 87127231192)
findPath(90000, 900000, 5994891682)
# sumVerification(route)
