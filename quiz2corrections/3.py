# first two numbers
num1 = int(input()) 
num2 = int(input())

print("Fibonacci sequence:")

for i in range(10):
    print(i)
    num3=num1+num2
    num1=num3
    num2=num2+num3#add code here