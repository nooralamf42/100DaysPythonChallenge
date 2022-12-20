# 🚨 Don't change the code below 👇
row1 = ["⬜️1", "⬜️2", "⬜️3"]
row2 = ["⬜️4", "⬜️5", "⬜️6"]
row3 = ["⬜️7", "⬜️8", "⬜️9"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇
new_position = position.split(",")
position1 = int(new_position[0])
position2 = int(new_position[1])

#Write your code above this row 👆
map[position1][position2] = "x"

# ## 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")