# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def rightrotation(r):
    m=len(r)
    z=r[m-1:]+r[:m-1]
    return z
def isrotation(x, y):
    a=[]
    b=[]
    while(x>0):
        a.append(x%10)
        x=x//10
    while(y>0):
        b.append(y%10)
        y=y//10
    # your code goes here
    n=len(a)
    for i in range(n):
        a=rightrotation(a)
        if(a==b):
            return True
    return False
	
	
