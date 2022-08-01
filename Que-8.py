# Write a Python program that accepts a string and calculate the number of digits and letters
# Sample Data : "Python 3.2"
# Expected Output :
# Letters 6 
# Digits 2

str = input("Enter a string: ")
letter=0
digit=0

for i in range(len(str)):
    # print(str[i])
    if((str[i]>='a' and str[i]>='z') or (str[i]>='A' and str[i]>='Z')):
        letter+=1
    elif(int(str[i]) in range(0,9)):
        digit+=1

print("Letters:", letter)
print("digits:",digit)