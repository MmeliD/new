
def int_to_string(num):
    if num==0:
        return 'zero'
    if num==1:
        return 'one'
    elif num==2:
        return 'two'
    elif num==3:
        return 'three'
    elif num==4:
        return 'four'
    elif num==5:
        return 'five'
    elif num==6:
        return 'six'
    elif num==7:
        return 'seven'
    elif num==8:
        return 'eight'
    elif num==9:
        return 'nine'
    elif num==9:
        return 'nine'
    else :
        return 'Please enter numbers in the range of 0 and 9' 


# Input handling, do not modify!
num = int(input())
print(int_to_string(num))