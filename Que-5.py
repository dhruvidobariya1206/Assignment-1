# Write a Python program to check a triangle is valid or not

a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))

if(a+b+c==180):
    print("It is a valid triangle.")
else:
    print("This triangle is invalid")