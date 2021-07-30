# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
	
    for i in l:
        row1=len(i)
        row2=len(l[0])
        if row1!=row2:
            return False
    return True



