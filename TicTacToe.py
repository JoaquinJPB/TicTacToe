from collections import deque

turn = deque(["O","X"])
table = [
	[" ", " ", " "],
	[" ", " ", " "],
	[" ", " ", " "],
]

def show_table():
    print("")
    for row in table:
        print (row)

def update_table(position,player):
    table[position[0]][position[1]] = player

def rotate_turn():
    turn.rotate()
    return turn[0]

def proccess_position(position):
    row,column = position.split(",")
    return [int(row)-1, int(column)-1]

def correct_position(position):
    if 0 <= position[0] <= 2 and 0 <= position[1] <= 2 :
        if table[position[0]][position[1]] == " ":
            return True
    return False

def winner(j):
	#Compara las filas del tablero
	if table[0] == [j,j,j] or table[1] == [j,j,j] or table[2] == [j,j,j]:
		return True
	#Compara las columnas
	elif table[0][0] == j and table[1][0] == j and table[2][0] == j:
		return True
	elif table[0][1] == j and table[1][1] == j and table[2][1] == j:
		return True
	elif table[0][2] == j and table[1][2] == j and table[2][2] == j:
		return True
	#Compara las diagonales
	elif table[0][0] == j and table[1][1] == j and table[2][2] == j:
		return True
	elif table[0][2] == j and table[1][1] == j and table[2][0] == j:
		return True
	return False

def game():
    show_table()
    player = rotate_turn()
    count = 0
    while True:
        position = input("It's up to {}.Choose a position (row,column) from 1 to 3: ".format(player))
        if position == 'exit':
            print("Exit Game")
            break
        try:
            position_l = proccess_position(position)
        except:
            print("Error,position is not valid {}".format(position))
            continue
        if correct_position(position_l):
            print("Correct")
            count += 1
            update_table(position_l,player)
            show_table()
            if winner(player):
                print("Player {} has won the game.".format(player))
                break
            elif count == 9 :
                print("The Game has been tie".format(player))
                break
            player = rotate_turn()
        else:
            print("Position {} is not correct".format(position))

game()