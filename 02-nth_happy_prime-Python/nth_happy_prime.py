# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def prime(k):
    if(k<2):
        return False
    elif(k==2):
        return True
    elif(k%2==0):
        return False
    else:
        for i in range(3,int((k**0.5)),2):
            if(k%i==0):
                return False
            
        return True

# print(prime(13))
def happy(k,n):
    sum=0
    temp=k
    
    while(temp>0):
        a=temp%10
        temp=temp//10
        sum+=((a)**2)
    if(sum==1 or sum==7):
        return True
    elif(sum<10):
        return False
    elif(sum==n):
        return False
        
    else:
        return happy(sum,n)  


def fun_nth_happy_prime(n):
    count=-1
    k=1
    while(True):
        if(prime(k)==True):
            if(happy(k,k)==True):
                count=count+1
            
            # print(n)
        if(count==n):
            return k   
        k=k+1
        
# print(nth(5))