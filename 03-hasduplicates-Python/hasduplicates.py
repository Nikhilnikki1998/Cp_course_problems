# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    x=[]
    for a in L:
        for b in a:
            x.append(b)
    x.sort()
    for a in range(len(x)-1):
        if(x[a]==x[a+1]):
            return True
    return False