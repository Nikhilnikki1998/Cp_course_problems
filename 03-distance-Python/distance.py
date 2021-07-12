# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.


def fun_distance(x1, y1, x2, y2):
	# your code goes here
	m=(x2-x1)**2
	n=(y2-y1)**2
	a=(m+n)**(1/2)
	# print(a)
	return (int(a))
# print(fun_distance(int(input()),int(input()),int(input()),int(input())))