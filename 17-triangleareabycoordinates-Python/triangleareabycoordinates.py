# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.
def distance(x1,y1,x2,y2):
	return (((x2-x1)**2 + (y2-y1)**2)**(1/2))

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	s1=distance(x1,y1,x2,y2)
	s2=distance(x2,y2,x3,y3)
	s3=distance(x1,y1,x3,y3)
	return trianglearea(s1,s2,s3)


def trianglearea(s1, s2, s3):
	# your code goes here
	peri=(s1+s2+s3)/2
	area=(peri*(peri-s1)*(peri-s2)*(peri-s3))**0.5
	return (area)