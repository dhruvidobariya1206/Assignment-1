# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly 
# right

import random
ran = random.randint(1, 9)
num = int(input("Enter a random number between 1(including) and 9(including):"))
if(num==ran):
    print("Guessed number is exactly right")
elif(num>ran):
    print("Guessed number is too high")
else:
    print("Guessed number is too low")