nums = {1, 3, 5, 7, 9, 11}
print("Original sets(nums): ",nums,"\n")
print("Test if 6 exists in nums:")
#print if 6 exists in nums
print({6}.issubset(nums))
print("Test if 7 exists in nums:")
#print if 7 exists in nums
print({7}.issubset(nums))
print("Test if 11 exists in nums:")
#print if 11 exists in nums
print({11}.issubset(nums))
print("Test if 0 exists in nums:")
#print if 0 exists in nums
print({0}.issubset(nums))
print("\nTest if 6 is not in nums")
#print if 6 is not in nums
if not {6}.issubset(nums):
    print(True)
else:
    print(False)
print("Test if 7 is not in nums")
#print if 7 is not in nums
if not {7}.issubset(nums):
    print(True)
else:
    print(False)
print("Test if 11 is not in nums")
#print if 11 is not in nums
if not {11}.issubset(nums):
    print(True)
else:
    print(False)
print("Test if 0 is not in nums")
#print if 0 is not in nums
if not {0}.issubset(nums):
    print(True)
else:
    print(False)


    ##EASY CORRECTIONS!!!!!________!!!!!!
nums = {1, 3, 5, 7, 9, 11}
print("Original sets(nums): ",nums,"\n")
print("Test if 6 exists in nums:")
print(6 in nums)
print("Test if 7 exists in nums:")
print(7 in nums)
print("Test if 11 exists in nums:")
print(11 in nums)
print("Test if 0 exists in nums:")
print(0 in nums)
print("\nTest if 6 is not in nums")
print(6 not in nums)
print("Test if 7 is not in nums")
print(7 not in nums)
print("Test if 11 is not in nums")
print(11 not in nums)
print("Test if 0 is not in nums")
print(0 not in nums)