# Write a Python program to find common items from two lists.
# input
# color1 = "Red", "Green", "Orange", "White"
# color2 = "Black", "Green", "White", "Pink"
# output
# {'Green', 'White'}

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
colors = [color1,color2]
comcol = list(set.intersection(*map(set, colors)))
print(comcol)