# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	len1=len(s1)
	len2=len(s2)
	si=""
	if(len1<len2):
		for i in range(len1):
			si=si+s1[i]+s2[i]
		si=si+s2[len1:]
	elif (len2<len1):
		for i in range(len2):
			si=si+s1[i]+s2[i]
		si=si+s1[len2:]
	else:
		for i in range(len1):
			si=si+s1[i]+s2[i]

	return si
	