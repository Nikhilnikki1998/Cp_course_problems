# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def check(x):
    a=10
    while(x):
        cnt=x%10
        x=x//10
        if(cnt>a):
            return False
        a=cnt
    return True   

def fun_nth_tidynumber(n):
    
    n=abs(n)
    cnt=0
    count=0
    while(cnt<=n):
        count=count+1
        if(check(count)):
            cnt=cnt+1
    return count
