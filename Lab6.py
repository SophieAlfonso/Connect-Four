# Sophie Alfonso UFID 94169614
# COP3502C Class 11724
# Lab 5: Connect Four

# This function creates the playing board given the number of rows and columns
def initialize_board(num_rows, num_cols):
    board = []          # Create an empty board

    for rows in range(num_rows):        # for each column in each row, add '-' to the row list
        row = []
        for cols in range(num_cols):
            row.append('-')
        board.append(row)       # append each row list to the board list

    return board        # return the board

# This function prints the board
def print_board(b):
    for row in range(len(b)-1,-1,-1):
        sect = b[row]                     # Create a temporary variable for the row being displayed
        for col in range(len(b[0])):      # Print each value in that row with a space between
            print(sect[col], end = ' ')
        print()                           # Start a new line

# This function puts the chip in the players desired column
def insert_chip(b, col, chip_type):
    for row in range(len(b)):       # Check each spot in a column starting from the bottom
        if b[row][col] ==  '-':     # if there isn't a token there yet, put the token there
            b[row][col] = chip_type
            break                   # break the loop
    return row                      # return the row in which the column was placed

# This function checks whether this turn resulted in a winning move, aka 4 in a row
def check_if_winner(b, col, row, chip_type):
    sr = 0                          # define a counting variable for each spot in a row
    for c in range(len(b[0])):
        if b[row][c] == chip_type:  # if there's a matching token there, add to the counter
            sr += 1
            if sr == 4:             # if the counter reaches 4 in a row, break the loop
                break
        else:
            sr = 0                  # if there's no matching token, reset the counter

    sc = 0                          # Repeat for each spot in a column
    for r in range(len(b)):
        if b[r][col] == chip_type:
            sc += 1
            if sc == 4:
                break
        else:
            sc = 0

    if sc == 4 or sr == 4:      # if four in a row was detected, return true, else false
        return True
    else:
        return False

# Define the main function
def main():
    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))

    board  = initialize_board(height, length)

    print_board(board)

    print('Player 1: x\n'       # Display each player's token
          'Player 2: o')

    winner = False
    num = 1                 # Create a variable to define each player's turn

    while not winner:       # Create a loop that runs until the game ends
        if num % 2 == 1:    # If num is odd, it's player 1's turn
            col = int(input('Player 1: Which column would you like to choose? '))
            chip = 'x'
        if num % 2 == 0:    # If num is even, it's player 2's turn
            col = int(input('Player 2: Which column would you like to choose? '))
            chip = 'o'

        row = insert_chip(board,col,chip)
        print_board(board)  # Print the board after each turn

        winner = check_if_winner(board, col, row, chip)

        if num ==  height * length:     # If the board is full, it's a tie, end the game
            print('Draw. Nobody wins.')
            break

        num += 1

    player = 1 if num % 2 == 0 else 2   # Determine the winning player by checking whether num is odd or even

    if winner:
        print(f'Player {player} won the game!')

# Call the main function
if __name__ == '__main__':
    main()