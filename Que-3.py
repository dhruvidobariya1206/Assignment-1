# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5 
# Expected Result : 615

num = int(input("Enter a number: "))
num2 = 10*num + num
num3 = 100*num+10*num+num

print(num+num2+num3)