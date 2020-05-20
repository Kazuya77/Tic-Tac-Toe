# write your code here
s = list(" " for i in range(9))
turn = 1
def win(pattern):
    if s[0] + s[1] + s[2] == pattern \
            or s[2] + s[5] + s[8] == pattern \
            or s[8] + s[7] + s[6] == pattern \
            or s[6] + s[3] + s[0] == pattern \
            or s[3] + s[4] + s[5] == pattern \
            or s[1] + s[4] + s[7] == pattern \
            or s[0] + s[4] + s[8] == pattern \
            or s[2] + s[4] + s[6] == pattern:
        return True
def show():
    print(f"""
    ---------
    | {s[0]} {s[1]} {s[2]} |
    | {s[3]} {s[4]} {s[5]} |
    | {s[6]} {s[7]} {s[8]} |
    ---------""")


while turn <= 9:
    coordinates = input("Enter the coordinates: ").split(" ")
    position = 8 + int(coordinates[0]) - 3 * int(coordinates[1])
    if position < 0 or position > 8:
        print("Coordinates should be from 1 to 3!")
        continue
    elif s[position] not in ("X", "O"):
        if turn % 2 == 0:
            s[position] = "O"
            turn += 1
            show()
            continue
        elif turn % 2 == 1:
            s[position] = "X"
            turn += 1
            show()
            continue
    elif s[position] in ("X", "O"):
        print("This cell is occupied! Choose another one!")
        continue
    else:
        print("You should enter numbers!")
        continue
if win("XXX"):
    print("X wins")
elif win("OOO"):
    print("O wins")
else:
    print("Draw")
