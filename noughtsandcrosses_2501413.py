import random
import os.path
import json
random.seed()

def draw_board(board):
    ''' Function draws board '''
    print('','-'*11)
    for i in board:
        print(f"| {i[0]} | {i[1]} | {i[2]} |")
        print('','-'*11)
    
def welcome(board):
    ''' Function welcomes user and idplay structure of board'''
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.")
    print("The board layout is shown below:")
    draw_board(board)
    print("When prompted, enter the number corresponding to the square you want.")

def initialise_board(board):
    '''Function initialize every element of board to space'''
    for i in range(0,3):
        for j in range(0,3):
            board[i][j]=' '
    return board
    
def get_player_move(board):
    '''Function prompt user for input to put X in the box'''
    while True:
        try:
            print(f"{'1 2 3':>25}")
            print(f"{'4 5 6':>25}")
            print("Choose your square: 7 8 9 ",end='')
            player=int(input(": "))
            if player in [1,2,3]:
                row=0
                col=player-1
            elif player in [4,5,6]:
                row=1
                col=player-4
            elif player in [7,8,9]:
                row=2
                col=player-7
            # return row and col
            return row, col
        except ValueError:
            continue
        except UnboundLocalError:
            continue

def choose_computer_move(board):
    '''Function choose the computer move according to the user'''
    for i in range(3):
        if (board[i][0]=='O' and board[i][1]=='O' and board[i][2]==' ')or(board[i][2]=='O' and board[i][1]=='O' and board[i][0]==' ')or(board[i][0]=='O' and board[i][2]=='O' and board[i][1]==' '):
            row=i
            col=board[i].index(' ')
            return row, col
        elif (board[0][i]=='O' and board[1][i]=='O' and board[2][i]==' ')or(board[2][i]=='O' and board[1][i]=='O' and board[0][i]==' ')or(board[0][i]=='O' and board[2][i]=='O' and board[1][i]==' '):
            row=next(j for j in range(3) if board[j][i]==' ')
            col=i
            return row, col
    if (board[0][0]=='O' and board[1][1]=='O' and board[2][2]==' ')or (board[0][0]=='O' and board[1][1]==' ' and board[2][2]=='O')or(board[0][0]==' ' and board[1][1]=='O' and board[2][2]=='O'):
        if board[0][0]==' ':
            return 0,0
        elif board[1][1]==' ':
            return 1,1
        elif board[2][2]==' ':
            return 2,2
    elif (board[0][2]=='O' and board[1][1]=='O' and board[2][0]==' ')or (board[0][2]=='O' and board[1][1]==' ' and board[2][0]=='O')or(board[0][2]==' ' and board[1][1]=='O' and board[2][0]=='O'):
        if board[0][2]==' ':
            return 0,2
        elif board[1][1]==' ':
            return 1,1
        elif board[2][0]==' ':
            return 2,0
    else:
        for i in range(3):
            if (board[i][0]=='X' and board[i][1]=='X' and board[i][2]==' ')or(board[i][2]=='X' and board[i][1]=='X' and board[i][0]==' ')or(board[i][0]=='X' and board[i][2]=='X' and board[i][1]==' '):
                row=i
                col=board[i].index(' ')
                return row, col
            elif (board[0][i]=='X' and board[1][i]=='X' and board[2][i]==' ')or(board[2][i]=='X' and board[1][i]=='X' and board[0][i]==' ')or(board[0][i]=='X' and board[2][i]=='X' and board[1][i]==' '):
                row=next(j for j in range(3) if board[j][i]==' ')
                col=i
                return row, col
        if (board[0][0]=='X' and board[1][1]=='X' and board[2][2]==' ')or (board[0][0]=='X' and board[1][1]==' ' and board[2][2]=='X')or(board[0][0]==' ' and board[1][1]=='X' and board[2][2]=='X'):
            if board[0][0]==' ':
                return 0,0
            elif board[1][1]==' ':
                return 1,1
            elif board[2][2]==' ':
                return 2,2
        elif (board[0][2]=='X' and board[1][1]=='X' and board[2][0]==' ')or (board[0][2]=='X' and board[1][1]==' ' and board[2][0]=='X')or(board[0][2]==' ' and board[1][1]=='X' and board[2][0]=='X'):
            if board[0][2]==' ':
                return 0,2
            elif board[1][1]==' ':
                return 1,1
            elif board[2][0]==' ':
                return 2,0
    aval=list()
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                aval.append([i,j])
    if [1,1] in aval:
        row,col=1,1
    elif [0,2] in aval:
        row,col=0,2
    elif [0,0] in aval:
        row,col=0,0
    elif [2,0] in aval:
        row,col=2,0
    elif [2,2] in aval:
        row,col=2,2
    else:
        cho=random.choice(aval)
        row,col=cho[0],cho[1]
    # and return row and col
    return row, col


def check_for_win(board, mark):
    '''Function is to validate whether user or computer has won or not'''
    for i in range(3):
        if board[i][0]==mark and board[i][1]==mark and board[i][2]==mark:
            return True
        elif board[0][i]==mark and board[1][i]==mark and board[2][i]==mark:
            return True
    if board[0][0]==mark and board[1][1]==mark and board[2][2]==mark:
        return True
    elif board[0][2]==mark and board[1][1]==mark and board[2][0]==mark:
        return True
    # return True if someone won, False otherwise
    return False

def check_for_draw(board):
    '''Function is used to check whether every box is occupied and headed for draw'''
    for i in range(3):
        if ' ' in board[i]:
            return False
    # return True if it is, False otherwise
    return True
        
def play_game(board):
    ''' develop code to play the game
     start with a call to the initialise_board(board) function to set
     the board cells to all single spaces ' '
     '''
    board=initialise_board(board)
    # then draw the board
    draw_board(board)
    # then in a loop, get the player move, update and draw the board
    while True:
        while True:
            row,col=get_player_move(board)
            if board[row][col]==' ':
                board[row][col]='X'
                break
            else:
                print("The square is taken")
        draw_board(board)
    # check if the player has won by calling check_for_win(board, mark),
        if check_for_win(board,'X'):
            return 1
    # if so, return 1 for the score
    # if not check for a draw by calling check_for_draw(board)
        if check_for_draw(board):          
    # if drawn, return 0 for the score
            return 0
    # if not, then call choose_computer_move(board)
    # to choose a move for the computer
    # update and draw the board
        row,col=choose_computer_move(board)
        board[row][col]='O'
        draw_board(board)
    # check if the computer has won by calling check_for_win(board, mark),
        if check_for_win(board,'O'):
            return -1
    # if so, return -1 for the score
    # if not check for a draw by calling check_for_draw(board)
        if check_for_draw(board):
            
    # if drawn, return 0 for the score
            return 0
    #repeat the loop
    return 0
                    
                
def menu():
    '''Function is used to show menu to user and promp input'''
    print("Enter one of the following options:")
    print('''1 - Play the game
2 - Save score in file 'leaderboard.txt'
3 - Load and display the scores from the 'leaderboard.txt'
q - End the program''')
    choice=input("1, 2, 3 or q? ")
    return choice

def load_scores():
    '''Function loads the leaderboard scores
    from the file 'leaderboard.txt'
     return the scores in a Python dictionary
     with the player names as key and the scores as values
     return the dictionary in leaders'''
    with open('leaderboard.txt','r')as file:
        tab=file.read()
        leaders=json.loads(tab)
    return leaders
    
def save_score(score):
    '''Function is used to save score of the player'''
    name=input("Enter your name")
    # and then save the current score to the file 'leaderboard.txt'
    with open('leaderboard.txt','r') as file:
        tab=file.read()
        leaderboard=json.loads(tab)
        leaderboard[name]=score
    with open('leaderboard.txt','w')as file:
        tab=json.dumps(leaderboard)
        file.write(tab)
def display_leaderboard(leaders):
    '''Function display the leaderboard scores
     passed in the Python dictionary parameter leader
     '''
    for i in leaders.keys():
        print(f"{i}={leaders[i]}")
        

