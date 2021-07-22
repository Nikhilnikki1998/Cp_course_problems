# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.
def listing(r,c):
    return [([0]*c) for x in range(r)]

def fun_matrixmultiply(m1, m2):
    a=len(m1)
    b=len(m2)
    for i in range(a):
        if len(m1[i])!=b:
            return None
    c=listing(a,len(m2[0]))
    for i in range(a):
        for j in range(len(m2[0])):
            c[i][j]=0
            for v in range(b):
                c[i][j]=c[i][j]+m1[i][v]*m2[v][j]
    return c




