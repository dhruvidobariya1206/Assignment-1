# Write a Python program to check a triangle is equilateral, isosceles or scalene.
# Note :
# An equilateral triangle is a triangle in which all three sides are equal.
# A scalene triangle is a triangle that has three unequal sides.
# An isosceles triangle is a triangle with (at least) two equal sides.

lens = input("Enter all three side separated by space:")
lens = lens.split(" ")
if(lens[0]==lens[1] and lens[2]==lens[1]):
    print("It is equilateral triangle.")
elif(lens[0]==lens[1] and lens[2]!=lens[0] or 
    lens[1]==lens[2] and lens[0]!=lens[1] or 
    lens[0]==lens[2] and lens[2]!=lens[1]):
    print("It is isosceles triangle.")
else:
    print("It is scalene triangle.")
