# Count the number of even and odd numbers from a series of numbers
# Input 
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Output
# Number of even numbers : 4 
# Number of odd numbers : 5

num = input("Enter numbers separated by space:")
num=num.split(" ")
even=0
odd=0
for n in num:
    if((int(n)%2)==0):
        even +=1
    else:
        odd += 1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)
