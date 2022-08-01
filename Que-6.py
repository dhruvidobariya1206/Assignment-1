# Write a Python program to construct the following pattern, using a nested loop number.
# 1 
# 22 
# 333 
# 4444 
# 55555 
# 666666 
# 7777777 
# 88888888 
# 999999999

num=9
r=0

while r<num:
    c=0
    while c<=r:
        print(r+1,end="")
        c+=1
    r+=1
    print("\n")