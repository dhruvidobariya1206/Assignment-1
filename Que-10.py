# Write a Python program to get the Fibonacci series between 0 to 50

x=0
y=1
z=0
z=x+y
print(x,y,end=" ")
while(z<50):
    # print(x,y)
    print(z,end=" ")
    x=y
    y=z
    z=x+y
    
    