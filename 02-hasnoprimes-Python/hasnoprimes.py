# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.


def prime(k):
    if(k<2):
        return False
    elif(k==2):
        return True
    elif(k%2==0):
        return False
    else:
        for i in range(3,int((k)),2):
            if(k%i==0):
                return False
            
        return True
    

def fun_hasnoprimes(l):
    for i in l:
        # print(i)
        for j in i :
            # print(j)
            if(prime(j)==True):
                return False
            
    return True
print(fun_hasnoprimes([[12,4,6],[8,12,14],[6,18]]))

