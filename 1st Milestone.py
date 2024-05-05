def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("---------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("---------")
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

def player_marker():
    player1_marker = ''

    while player1_marker != 'x' and player1_marker != 'o':
        player1_marker = input("Player1 choose your marker 'x' or 'o': ")

        if player1_marker != 'x' and player1_marker != 'o':
            print("Wrong choice!")

    if player1_marker == 'x':
        player2_marker = 'o'
    else:
        player2_marker = 'x'

    print("Player1 marker: ", player1_marker, '\n', "Player2 marker: ", player2_marker)

    return (player1_marker, player2_marker)


def user1_input():
    player1 = ''
    choice = False

    while player1.isdigit() == False or choice == False:
        player1 = input("Player1 choose position (1-9): ")
        if player1.isdigit() == False:
            print('Invalid choice')
        if player1.isdigit() == True:
            if int(player1) in range(1, 10):
                choice = True
            else:
                print('Invalid choise')

    return int(player1)

def user2_input():
    player2 = ''
    choice = False

    while player2.isdigit() == False or choice == False:
        player2 = input("Player2 choose position (1-9): ")
        if player2.isdigit() == False:
            print('Invalid choice')
        if player2.isdigit() == True:
            if int(player2) in range(1, 10):
                choice = True
            else:
                print('Invalid choice')
    return int(player2)


def position1(position,player):

    board[position] = player


def check(result):
    for i in range(1,8,3):
        if ' ' not in board[i:i+3]:

            if 'x' not in board[i:i+3] or 'o' not in board[i:i+3] :
                result = False
                return result

    for i in range(1,4):
        if ' ' not in board[i:i+7:3]:
            if 'x' not in board[i:i+7:3] or 'o' not in board[i:i+7:3]:
                result = False
                return result

    if ' ' not in board[1::4]:
        if 'x' not in board[1::4] or 'o' not in board[1::4]:
            result = False
            return result
        else:
            result = True

    if ' ' not in board[3:8:2]:
        if 'x' not in board[3:8:2] or 'o' not in board[3:8:2]:
            result = False
            return result
        else:
            result = True

    if ' ' not in board:
        result = False
        return result

    else:
        return result


# Execution:

x = input('Want to play a game? (Y/N): ')
while x == 'Y' or x == 'y':

    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    display_board(board)

    player1 , player2 = player_marker()

    result = True
    while result:

        p = user1_input()
        position1(p ,player1)
        result = check(result)
        display_board(board)


        p = user2_input()
        position1(p , player2)
        result = check(result)
        display_board(board)


    print()
    print('_____________')
    print('Game Over')
    print('Thank you for Playing!')
    x = input('Want to play again? (Y/N): ')
print('Come back soon!!')
