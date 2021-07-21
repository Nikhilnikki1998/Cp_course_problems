# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.

def sum(a,i,b):
    if(len(a)==i):
        return b
    elif(i%2==0):
        b=b+a[i]
        return sum(a,i+1,b)
    else:
        b=b-a[i]
        return sum(a,i+1,b)


def fun_alternatingsum(a): 
	 return sum(a,0,0)


