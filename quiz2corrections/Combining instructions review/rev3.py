#Write a function that returns "a is greater than b", "a is less than b", or "a is equal to b" depending on the values of two int input params a and b.
def a_vs_b(a,b):
	# your code here
	if a > b:
	    return "a is greater than b"
	elif a < b:
	    return "a is less than b"
	else:
	    return "a is equal to b"

# Input handling, do not modify!
 input_parts = input().split(" ")
 a = int(input_parts[0])
 b = int(input_parts[1])
 print(a_vs_b(a, b))