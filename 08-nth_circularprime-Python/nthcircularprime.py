# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False

    return True
def length(n):
    count=0
    while(n>0):
        count=count+1
        n=n//10
    return count
def circular(n):
    x=length(n)
    cnt=x
    while cnt>0:
        temp=n%10
        n=n//10
        n=temp*(10**(x-1))+n
        if isprime(n):
            cnt=cnt-1
        else:
            return False
    return True
def nthcircularprime(x):
    n=abs(x)
    cnt=1
    temp=0
    while(cnt<=n):
        temp=temp+1
        if(isprime(temp) and circular(temp)):
            cnt=cnt+1
    return temp