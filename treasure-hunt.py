# the grid is made of 3x3 cells
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
# each line makes up a row in a grid
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot. e.g. A1 for the top left cell.")
position = input("Where do you want to put the treasure? ")

# place the treasure in the chosen cell
if position[1] == "1" and position[0] == "A":
  map[0][0] = "X"
elif position[1] == "1" and position[0] == 'B':
  map[0][1] = 'X'
elif position[1] == "1" and position[0] == 'C':
  map[0][2] = 'X'
elif position[1] == "2" and position[0] == 'A':
  map[1][0] = 'X'
elif position[1] == "2" and position[0] == 'B':
  map[1][1] = 'X'
elif position[1] == "2" and position[0] == 'C':
  map[1][2] = 'X'
elif position[1] == "3" and position[0] == 'A':
  map[2][0] = 'X'
elif position[1] == "3" and position[0] == 'B':
  map[2][1] = 'X'
elif position[1] == "3" and position[0] == 'C':
  map[2][2] = 'X'
else:
  # if the position doesn't match the dimensions of the grid, print an error message
  print("This is an incorrect input.")

# print the new grid with the hidden treasure
print(f"{line1}\n{line2}\n{line3}")