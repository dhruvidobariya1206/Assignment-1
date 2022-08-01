# Write a Python program to construct the following pattern, using a nested for loop.
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

num=5
r=0

while r<num:
    c=0
    while c<=r:
        print("*",end="")
        c+=1
    r+=1
    print("\n")
num-=1
r=0
while r<num:
    c=0
    while c<=num-r-1:
        print("*",end="")
        c+=1
    r+=1
    print("\n")