# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def tidy(n):
    a=n%10
    b=n//10
    if(a>b):
        return True
    else:
        return False

def fun_nth_tidynumber(n):
    count=-1
    if(n==0):
        return 1
    if(tidy(n)==True):
        count=count+1
    if(count==n):
        return count
print(fun_nth_tidynumber(1))