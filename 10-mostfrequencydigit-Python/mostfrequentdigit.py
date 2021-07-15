# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	if n==0:
		return 0
	n=abs(n)
	count=n
	m=0
	k=0
	while n>0:
		temp=count
		a=n%10
		verify=0
		while temp>0:
			b=temp%10
			if b==a:
				verify=verify+1
			temp=temp//10
		if m<verify:
			m=verify
			k=a
		if m==verify:
			if a<k:
				k=a
		n=n//10
	return k
	