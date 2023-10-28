def game():

turn = 'X'
count = 0

for i in range(10):
    printBoard(theBoard)

    move = input(f"It's your turn, {turn}. Move to which place?")        

    if theBoard[move] == ' ':
        theBoard[move] = turn
        count += 1
    else:
        print("That place is already filled.\nMove to which place?")
        continue

    # Now we will check if player X or O has won,for every move after 5 moves. 
    if count >= 5:
        if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
            win_message(turn)              
            break
        elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
            win_message(turn) 
            break
        elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
            win_message(turn) 
            break
        elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
            win_message(turn) 
            break
        elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
            win_message(turn) 
            break
        elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
            win_message(turn) 
            break 
        elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
            win_message(turn) 
            break
        elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
            win_message(turn) 
            break 

    # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if count == 9:
        print("\nGame Over.\nIt's a Tie!!")                

    # Now we have to change the player after every move.
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'        

# Now we will ask if player wants to restart the game or not.
restart = input("Do want to play Again?(y/n) ")
if restart in ('y', 'Y'):  
    for key in board_keys:
        theBoard[key] = " "

    game()
if name == "main": game()
