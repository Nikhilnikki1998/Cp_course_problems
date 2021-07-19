# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
	digit=abs(digit)
	if(k==0):
		a=digit%10
		return a
	else:
		a=digit//((10)**k)
		a=a%10
		return a
