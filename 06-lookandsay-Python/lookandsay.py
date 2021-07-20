# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	    # your code goes here
    temp= 1
    li=[]
    n=len(a)
    for i in range(n-1):
        if(a[i]!=a[i+1]):
            li.append((temp,a[i]))
            temp=1
            
        else:
            temp = temp+1
    if(n!=0):
        li.append((temp,a[n-1]))
    return li 
