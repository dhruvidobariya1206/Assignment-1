# Write a Python program to check whether an alphabet is a vowel or consonant

char = input("enter a character: ")
char = char.lower()
if(len(char)>1):
    print("Enter one character")
elif(char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
    print("character is a vowel")
else:
    print("character is a consonant")