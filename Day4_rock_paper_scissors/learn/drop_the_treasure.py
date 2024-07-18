print("Treasure Dropper")

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("\n Where do you want to put the treasure? \n Specify in row and column number. \n eg. 23 => 2nd row and 3rd column:\n")

row = int(position[0]) - 1
column = int(position[1]) - 1

map[row][column] = "X"

print(f"{row1}\n{row2}\n{row3}")
