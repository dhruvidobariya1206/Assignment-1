# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date
name=input("Enter your name: ")
age=int(input("Enter your age: "))

tdate=date.today()
tyear=tdate.year
# print(type(tdate))
year = tyear+(100-age)
print(name,"will turn 100 in year",year)