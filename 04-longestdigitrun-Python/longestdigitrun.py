# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(x):
    x=abs(x)
    if x==0:
        return 0

    a=0
    temp=1
    for i in range(10):
        b=10
        c=x
        count=0
        while(c>0):
            y=c%10
            c=c//10
            if y==b and y==i:
                count=count+1
            b=y
        if(count>a):
            a=count
            temp=i
    return temp