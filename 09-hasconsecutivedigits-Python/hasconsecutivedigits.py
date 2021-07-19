# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that 
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
	# your code goes here
    n=abs(n)
    temp=1
    while n>0:
        dummy=n%10
        n=n//10
        if dummy==temp:
            return True
        temp=dummy
    return False

	