# Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 
# and 2700
i=1500
arr = []
for i in range(1500,2701):
    if(i%35==0):
        arr.append(i)
    i+=1
print(arr)